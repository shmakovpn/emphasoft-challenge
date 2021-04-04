"""
This script fetches a list of all available Form names

Author: shmakovpn
Date: 2021-04-04
"""
from typing import Coroutine, List, Any, Match, Pattern, Optional
from aiohttp.client import ClientSession, ClientResponse, ClientConnectionError
import asyncio
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
import re

FetchFunc = Coroutine[Any, Any, str]
page_id_pattern: Pattern[str] = re.compile(r'(?P<page_id>\d+)$')


def irs_url(page_num: int) -> str:
    return f'https://www.irs.gov/downloads/irs-pdf?page={page_num}'


def page_id_from_url(url: str) -> int:
    match_id: Optional[Match[str]] = page_id_pattern.search(url)
    assert match_id
    page_id: str = match_id.group('page_id')
    assert page_id
    return int(page_id)


class FormRecord:
    tag: Tag
    filename: str = ''
    url: str = ''
    date: str = ''
    descripton: str = ''

    def __init__(self, tag: Tag) -> None:
        self.tag = tag
        self.filename = self.tag.get('filename')
        tds: ResultSet = self.tag.find_all('td')
        if len(tds) == 4:
            self.url = tds[0].find('a').get('href')
        print(self.url)


class Page():
    url: str = ''
    _html: str = ''
    session: ClientSession  # static
    # form_records:  List[]

    def __init__(self, url: str) -> None:
        self.url = url

    async def _fetch(self) -> str:
        response: ClientResponse
        try:
            async with self.session.get(self.url) as response:
                return await response.text()
        except ClientConnectionError as e:
            print(f'Error: fetching url="{self.url}" was failed: {e}')
            return ''

    async def html(self) -> str:
        if self._html:
            return self._html
        self._html = await self._fetch()
        return self._html


class FirstPage(Page):
    _last_page_id: int = -1

    async def last_page_id(self) -> int:
        if self._last_page_id >= 0:
            return self._last_page_id
        html: str = await self.html()
        assert html
        soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
        last_anchors: ResultSet = soup.select(
            '.pager__item.pager__item--last a')
        assert len(last_anchors) == 1
        last_anchor: Tag = last_anchors[0]
        last_anchor_href: str = last_anchor.get('href', '')
        assert last_anchor_href
        self._last_page_id = page_id_from_url(last_anchor_href)
        return self._last_page_id


async def main():
    first_page_url: str = irs_url(0)
    async with ClientSession() as Page.session:
        first_page: Page = FirstPage(first_page_url)
        last_page_id: int = await first_page.last_page_id()
        assert last_page_id >= 0
        page_id: int
        tasks: List[FetchFunc] = []
        pages: List[Page] = []
        pages.append(first_page)
        for page_id in range(1, last_page_id+1):
            page: Page = Page(irs_url(page_id))
            pages.append(page)
            tasks.append(page.html())
        _ = await asyncio.gather(*tasks)
        records: List[FormRecord] = []
        for page in pages:
            html = await page.html()
            soup: BeautifulSoup = BeautifulSoup(html, 'html.parser')
            page_records: ResultSet = soup.select('table.tablesaw tr[filename]')
            for record in page_records:
                form_record: FormRecord = FormRecord(record)
                records.append(form_record)



if __name__ == '__main__':
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    loop.run_until_complete(main())
