"""
This script fetches a list of all available Form names
using sitemap.xml

Author: shmakovpn
Date: 2021-04-04
"""
from typing import Coroutine, Dict, List, Any, Tuple
from aiohttp.client import ClientSession, ClientResponse, ClientConnectionError
import asyncio
import aiofiles
from bs4 import BeautifulSoup
from bs4.element import ResultSet
import hashlib
import os
from datetime import datetime
import json

FetchFuncStr = Coroutine[Any, Any, str]
FetchFuncListStr = Coroutine[Any, Any, List[str]]
SITE_URL: str = 'https://www.irs.gov/'
ROOT_SITEMAP_URL: str = f'{SITE_URL}/sitemap.xml'
SCRIPT_DIR: str = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR: str = os.path.join(SCRIPT_DIR, 'cache')
current_year: int = datetime.now().year


class Page():
    url: str = ''
    _content: str = ''
    session: ClientSession  # static

    def __init__(self, url: str) -> None:
        self.url = url

    def _url_hash(self) -> str:
        return hashlib.md5(self.url.encode('utf-8')).hexdigest()

    def _cache_filename(self) -> str:
        return os.path.join(CACHE_DIR, self._url_hash())

    async def _fetch_from_cache(self) -> str:
        cache_filename: str = self._cache_filename()
        if os.path.isfile(cache_filename):
            async with aiofiles.open(cache_filename, mode='r') as f:
                return await f.read()
        return ''  # return an empty string if cache does not exist

    async def _fetch_from_internet(self) -> str:
        response: ClientResponse
        try:
            async with self.session.get(self.url) as response:
                return await response.text()
        except ClientConnectionError as e:
            print(f'Error: fetching url="{self.url}" was failed: {e}')
            return ''  # return an empty string if an error has occurred

    async def _save_to_cache(self, content: str) -> None:
        cache_filename: str = self._cache_filename()
        async with aiofiles.open(cache_filename, mode='w') as f:
            await f.write(content)

    async def _fetch(self) -> str:
        cache_content: str = await self._fetch_from_cache()
        if cache_content:
            return cache_content
        return await self._fetch_from_internet()

    async def content(self) -> str:
        if self._content:
            return self._content
        self._content = await self._fetch()
        await self._save_to_cache(self._content)
        return self._content


class Sitemap(Page):
    sitemap_urls: List[str]

    def __init__(self, url: str) -> None:
        super().__init__(url)
        self.sitemap_urls = []
    
    async def urls(self) -> List[str]:
        if self.sitemap_urls:
            return self.sitemap_urls
        content: str = await self.content()
        soup: BeautifulSoup = BeautifulSoup(content, 'html.parser')
        locations: ResultSet = soup.find_all('loc')
        for location in locations:
            self.sitemap_urls.append(location.get_text())
        return self.sitemap_urls


class RootSitemap(Sitemap):
    def __init__(self, url: str = ROOT_SITEMAP_URL) -> None:
        super().__init__(url)


def url_filter(url: str) -> bool:
    if not url.endswith('.pdf'):
        return False
    if url.startswith('https://www.irs.gov/pub/irs-prior/f') or url.startswith('https://www.irs.gov/pub/irs-pdf/f'):
        return True
    return False


class Form:
    min_year: int = current_year
    max_year: int = 0
    code: str = ''
    
    @staticmethod
    def parse_url(url: str) -> List[str]:
        url_parts: List[str] = url.split('/')
        filename: str = url_parts.pop()[1:].rsplit('.', 1)[0]
        return filename.split('--')
    
    def __init__(self, code_year: List[str]):
        self.code = code_year[0]
        self.update(code_year)
    
    def update(self, code_year: List[str]) -> None:
        year: int = current_year
        if len(code_year) > 1:
            year = int(code_year[1])
        if self.max_year < year:
            self.max_year = year
        if self.min_year > year:
            self.min_year = year
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'code': self.code,
            'min_year': self.min_year,
            'max_year': self.max_year,
        }
    
    def __str__(self) -> str:
        return json.dumps(self.to_dict())


class FormJson(Form):
    def __init__(self, form_json: Any) -> None:
        self.min_year = form_json['min_year']
        self.max_year = form_json['max_year']
        self.code = form_json['code']
    

async def get_urls_filtered() -> List[str]:
    urls_filtered: List[str]
    urls_cache: str = os.path.join(CACHE_DIR, 'urls_cache.txt')
    if os.path.isfile(urls_cache):
        with open(urls_cache, 'r') as f:
            urls_filtered = f.readlines()
    else:
        async with ClientSession() as Page.session:
            root_sitemap: RootSitemap = RootSitemap()
            sitemap_urls: List[str] = await root_sitemap.urls()
            sitemaps: List[Sitemap] = []
            tasks: List[FetchFuncListStr] = []
            for sitemap_url in sitemap_urls:
                sitemap: Sitemap = Sitemap(sitemap_url)
                sitemaps.append(sitemap)
                tasks.append(sitemap.urls())
            urls: List[str] = []  # all urls from sitemaps
            urls_list: Tuple[List[str]] = await asyncio.gather(*tasks)
            for url_list_item in urls_list:
                urls += url_list_item
            urls_filtered: List[str] = list(filter(url_filter, urls))
            with open(urls_cache, 'w') as f:
                f.write('\n'.join(urls_filtered))
    return urls_filtered


async def get_forms() -> Dict[str, Form]:
    forms_cache: str = os.path.join(CACHE_DIR, 'form_cache.json')
    forms: Dict[str, Form] = {}
    if os.path.isfile(forms_cache):
        with open(forms_cache, 'r') as f:
            forms_cache_content: str = f.read()
            forms_cache_obj: Any = json.loads(forms_cache_content)
            for code in forms_cache_obj:
                forms[code] = FormJson(forms_cache_obj[code])
    else:
        urls_filtered: List[str] = await get_urls_filtered()
        for url in urls_filtered:
            code_year: List[str] = Form.parse_url(url)
            if code_year[0] in forms:
                forms[code_year[0]].update(code_year)
            else:
                forms[code_year[0]] = Form(code_year)
        forms_dict: Dict[str, Any] = {}
        for code in forms:
            forms_dict[code] = forms[code].to_dict()
        with open(forms_cache, 'w') as f:
            f.write(json.dumps(forms_dict, indent=2))
    return forms


async def main():
    forms: Dict[str, Form] = await get_forms()
    print(len(forms))
        


if __name__ == '__main__':
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    loop.run_until_complete(main())
