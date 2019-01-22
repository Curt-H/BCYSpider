# -*- coding: utf-8 -*-

from utils import log
from modules import page

if __name__ == '__main__':
    log('Start')
    r = page.get_content('https://bcy.net')
    log(r)
