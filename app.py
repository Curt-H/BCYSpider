# -*- coding: utf-8 -*-
import time

from utils import log
# from modules import cache, login
# from modules.following import get_following_list
from modules.cache import get_content
from modules.washer_star import get_actor_info

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
        html_content = get_content(site.strip(), settings=SETTINGS)
        # get_actor_info(html_content)

        log(html_content)
