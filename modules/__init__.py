import os

from utils import load_str, log


def generate_headers():
    # these should be written by user
    cookies = load_str('data/user/cookie.txt')
    user_agent = load_str('data/user/user-agent.txt')

    headers = {
        'user-agent': user_agent,
        'Cookie': cookies
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


def dump_file(filename: str, content, path, mode='w+'):
    fname = '\\'.join([path, filename])
    log(fname)
    c = content

    if check_if_path_exists(path) and filename.find('info') < 0:
        mode = 'a+'
    with open(fname, mode, encoding='utf-8-sig') as f:
        f.write(c)


def check_if_path_exists(path):
    p = path
    if not os.path.exists(p):
        log('not exists')
        os.makedirs(p)
        return False
    return True
