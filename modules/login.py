import requests

from modules import generate_headers
from utils import log


def log_in():
    """
    this module is designed to deal with login problems
    but for now, it need to load cookie file to login in, which user must manually copy the cookie to local file
    """
    # from file to load cookie and user-agent

    log('Try to log in')
    # Get user homepage to check if login is successful
    r = requests.get('https://bcy.net/u/1015748', headers=generate_headers())
    # log(r.text)
