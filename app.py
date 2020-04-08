# -*- coding: utf-8 -*-
import time

from modules import dump_to_txt
from modules.url_parse import url_parser
from modules.washer_serial import get_items_info
from utils import log
from modules.cache import get_content

# from requests import *

if __name__ == '__main__':
    log('start')
    SETTINGS = {
        'proxies': {
            "http": "http://127.0.0.1:10801",
            'https': 'https://127.0.0.1:10801'
        },
        'headers': {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/67.0.3396.79 Safari/537.36',
            'Connection': 'close'
        }
    }

    # Read urls from files
    with open('website.txt', 'r+', encoding='utf-8') as f:
        web_sites = f.readlines()
        log(f'Find {len(web_sites)} url(s)')

    # Catch url page and get the content
    for site in web_sites:
        task_info = dict()
        task_info['url'] = site.strip()
        task_info['type'], task_info['code'] = url_parser(task_info['url'])
        task_info['html'] = get_content(task_info['url'], settings=SETTINGS)
        result = get_items_info(task_info)
        answer = dump_to_txt(result)
        if answer == 0:
            log('Finished')
