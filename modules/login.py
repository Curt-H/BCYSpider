import requests
import json
from utils import log, load_str


def log_in():
    """
    this module is designed to deal with login problems
    but for now, it need to load cookie file to login in, which user must manually copy the cookie to local file
    """
    # from file to load cookie and user-agent
    cookies = load_str('data/user/cookie.txt')
    user_agent = load_str('data/user/user-agent.txt')
    headers = {
        'user-agent': user_agent,
        'Cookie':     cookies
    }

    log('Try to log in')
    # Get user homepage to check if login is successful
    r = requests.get('https://bcy.net/u/1015748', headers=headers)
    log(r.text)
