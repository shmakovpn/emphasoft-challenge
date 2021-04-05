# EmphaSoft challenge

## Python version

Python 3.8.5

## Task 1 data

Please look at the *task1_data.py*.

## Task 1 execution

```bash
python task1.py
```

## Задача 1 комментарии

- Не все формы могут быть найдены поиском на сайте. Поэтому используется парсинг файлов sitemap.
Т.к. файлов sitemap несколько, используется параллельная загрузка средствами asyncio/aiohttp.

- Есть возможность работы за прокси (как раз мой случай). Для этого необходимо создать файл proxy.py в корне проекта.
    ```python
    from typing import Dict, Any

    proxy_args: Dict[str, Any] = {
        'ssl': False,
        'proxy': 'http://ip:port',
    }  
    ```

- Предусмотрено кэширование. Чтобы избежать повторных запросов. Т.к. судя по sitemap, обновления на сайте происходят очень редко.
Чтобы удалить кэш, надо очистить папку cache

- Не для всех форм существует описание на сайте. Поэтому для получения form_title выгружается и парсится PDF.

- Не все PDF файлы можно разобрать. Данный кейс также представлен в тестовом наборе данных.
Я думаю, что обработка таких файлов выходит за текущей рамки задачи. Но если есть такая необходимость, можно поработать и в этом направлении.

- Скрипт, способен находить даже форму, уже выведенные из эксплуатации.

## The story

In US, taxes are often complex and require many different PDF forms and posted informational
notices. IRS service keeps records of the current tax year's forms and historical forms going back
many years online on [irs.gov](https://irs.gov).

## Challenge

For this challenge you must write two different utilities for searching IRS tax forms:

- Taking a list of tax form names (ex: "Form W-2", "Form 1095-C"), search the website and
return some informational results. Specifically, you must return the "Product Number", the
"Title", and the maximum and minimum years the form is available for download. The
results should be returned as json, in the format of the following example:
    ```json
    [
      {
        "form_number": "Form W-2",
        "form_title": "Wage and Tax Statement (Info Copy Only)",
        "min_year": 1954,
        "max_year": 2021
      }
      ...
    ]
 ```
- Taking a tax form name (ex: "Form W-2") and a range of years (inclusive, 2018-2020 should
fetch three years), download all PDFs available within that range. The downloaded PDFs
should be downloaded to a subdirectory under your script's main directory with the name of
the form, and the file name should be the "Form Name - Year" (ex: Form W-2/Form W-2 -
2020.pdf ).

## Requirements

The challenge must be written in Python 3 and can use any publicly available library. If you use any
non-standard libraries, you MUST include a standard pip-compatible "requirements.txt" file outlining
every requirement needed to run your script(s).

You may use any method for taking input and returning required output from your script (command
line arguments, command line input, files, etc.)

You must include a README.txt file explaining which specific version of Python is used (ex: Python
3.8.0), how to properly run your script (including how it takes input parameters and how it outputs
JSON for part 1.) Also feel free to use this README.txt to add any additional info you'd like to share
about your script or any feedback on the challenge itself.

