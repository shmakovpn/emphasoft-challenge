"""
This script fetches a list of all available Form names
using sitemap.xml

Author: shmakovpn
Date: 2021-04-04
"""
from typing import List, Set
import os
import asyncio
import aiofiles
from aiohttp.client import ClientSession
# task2 data
from task2_data import task2_data
from task1 import parse_task_code, get_forms, Form, PdfPage

# proxy configuration
try:
    from proxy import proxy_args
except ImportError:
    proxy_args: Dict[str, Any] = {}

SITE_URL: str = 'https://www.irs.gov/'
SCRIPT_DIR: str = os.path.dirname(os.path.abspath(__file__))
TASK2_DIR: str = os.path.join(SCRIPT_DIR, 'task2')

if not os.path.isdir(TASK2_DIR):
    os.mkdir(TASK2_DIR)


def get_range(range_list: List[int]):
    assert len(range_list) == 2
    range_list.sort()
    return range(range_list[0], range_list[1] + 1)


async def main():
    forms: Dict[str, Form] = await get_forms()
    for task_code in task2_data:
        parsed_task_code: str = parse_task_code(task_code)
        if parsed_task_code not in forms:
            print(f'Error: task code {parsed_task_code} does not exist')
        else:
            form: Form = forms[parsed_task_code]
            req_range: range = get_range(task2_data[task_code])
            exist_range: range = get_range([form.min_year, form.max_year])
            no_pdf_set: Set[int] = set(req_range) - set(exist_range)
            yes_pdf_set: Set[int] = set(req_range) & set(exist_range)
            if len(no_pdf_set):
                print(f'{task_code}. No PDFs for year(s): {no_pdf_set}')
            if not len(yes_pdf_set):
                print('{task_code}. No years to load')
            else:
                for year in yes_pdf_set:
                    async with ClientSession() as PdfPage.session:
                        pdf_page: PdfPage = PdfPage(form.url_year(year))
                        content: bytes = await pdf_page.content()
                        folder: str = os.path.normpath(
                            os.path.join(TASK2_DIR, task_code))
                        if not os.path.isdir(folder):
                            os.mkdir(folder)
                        filename: str = f'{task_code} - {year}.pdf'
                        file_path: str = os.path.normpath(os.path.join(folder, filename))
                        async with aiofiles.open(file_path, mode='wb') as f:
                            await f.write(content)
                            print(f'{filename} successfully created')


if __name__ == '__main__':
    loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
    loop.run_until_complete(main())