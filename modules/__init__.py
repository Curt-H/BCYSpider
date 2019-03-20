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


def generate_coser_url(coser_id):
    """
    generate coser homepage url with coser id input
    :param coser_id: string
    :return: url: string
    """
    c = coser_id
    return f'https://bcy.net/u/{c}/post'

def generate_post_url(post_id):
    p = post_id
    return f'https://bcy.net/item/detail/{p}'
