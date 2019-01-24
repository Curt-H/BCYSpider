from utils import load_str


def generate_headers():
    # these should be written by user
    cookies = load_str('data/user/cookie.txt')
    user_agent = load_str('data/user/user-agent.txt')

    headers = {
        'user-agent': user_agent,
        'Cookie':     cookies
    }
    return headers
