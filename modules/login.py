import requests
import json
from utils import log


def log_in():
    """
    this module is designed to deal with login problems
    but for now, it need to load cookie file to login in, which user must manually copy the cookie to local file
    """
    log('Try to log in')
    with open('cookie.json', 'r', encoding='utf-8') as f:
        cookie = json.load(f)
    r = requests.get('https://bcy.net/u/110606662197', cookie=cookie)
    log(r.text)
