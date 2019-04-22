# -*- coding: utf-8 -*-

from utils import log
from modules import cache, login
from modules.following import get_following_list
from modules.data_wash import get_posts_list, save_pics_from_each_post
from requests import *

if __name__ == '__main__':
    log('Start')
    # r = page.get_content('https://bcy.net')
    # log(r)
    # https://bcy.net/passport/web/user/login/?account_sdk_source=web
    # login.log_in()
    # get_following_list()
    post_list = get_posts_list('446923')
    save_pics_from_each_post(post_list)
