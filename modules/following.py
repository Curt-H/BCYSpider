"""
this module is design to dealing with following coser management
"""
from modules import generate_headers
from modules.cache import get_content
from utils import log


def get_following_list(user_id=1015748):
    ui = user_id
    url = f'https://bcy.net/u/{ui}/following'
    content = get_content(url)
    log(content)
