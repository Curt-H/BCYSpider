import time

import chardet
from pyquery import PyQuery as pq
from modules.cache import get_content
from modules import generate_coser_url, generate_post_url, dump_file
from utils import log
from html import unescape
import json


def get_actor_info(html):
    result = dict()

    content = pq(html)
    photo_info = content('.photo-info')
    photo_frame = content('.photo-frame')
    # log(type(photo_info))
    # log(photo_info.text())
    c = [p for p in photo_info.items()]
    name = get_actor_name(c[0])

    get_movie_info(content, name)
    return 0


def get_actor_name(content: pq):
    name = content('.pb10').text()
    other_info = [p.text() for p in content('p').items()]
    log(name, other_info)

    txt_content = '\n'.join([name, *other_info])
    dump_file(f'{name}-info.txt', txt_content, path=f'data', mode='w')

    log(txt_content)
    return name


def get_movie_info(content: pq, name):
    c = content
    csv_content = ""
    img = c('.photo-frame')('img')
    photo_info = [p for p in c('.photo-info').items()]

    for index, i in enumerate(img.items()):
        if index == 0:
            continue
        date = photo_info[index]('date')
        info = [d.text() for d in date.items()]
        seriea_no, publish_date = info
        title = i.attr('title')
        log(title, seriea_no, publish_date)
        csv_content += f'{seriea_no}\t{title}\t{publish_date}\n'
    dump_file(f'{name}.txt', csv_content, path=f'data')

    log(csv_content)
