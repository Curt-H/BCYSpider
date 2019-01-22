# -*- coding: utf-8 -*-

from utils import log
from modules import page
from requests import *

if __name__ == '__main__':
    log('Start')
    # r = page.get_content('https://bcy.net')
    # log(r)
    # https://bcy.net/passport/web/user/login/?account_sdk_source=web
    data = dict(
        account='15695618017',
        password='FFF000123'
    )
    log(data)

    r = post('https://bcy.net/passport/web/user/login/?account_sdk_source=web', data=data)
    log(r.text)
