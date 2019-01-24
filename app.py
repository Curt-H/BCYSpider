# -*- coding: utf-8 -*-

from utils import log
from modules import cache, login
from modules.following import get_following_list
from requests import *

if __name__ == '__main__':
    log('Start')
    # r = page.get_content('https://bcy.net')
    # log(r)
    # https://bcy.net/passport/web/user/login/?account_sdk_source=web
    login.log_in()
    get_following_list()
