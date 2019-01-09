# -*- coding: utf-8 -*-

from utils import log
from modules.page import cached_url

if __name__ == '__main__':
    log('Start')
    r = cached_url('https://www.baidu.com', 'test.txt')

    log(r)
