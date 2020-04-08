from utils import log


def url_parser(url_parsing):
    """
    Confirm url kind and start the washer
    :param url_parsing: url
    """

    # find which the url kind
    url = url_parsing
    url_part_list = url.split('/')
    url_index = url_part_list.index('www.javbus.com')
    spider_type = url_part_list[url_index + 1]
    code = url_part_list[url_index + 2]

    url_parts = {
        'type': spider_type,
        'code': code
    }

    log(f'Raw url is [{url}]')
    log(f'Spider type is [{spider_type}]')

    return data_washer[spider_type](url_parts)


def get_serials_title(url_parts: dict):
    u = url_parts

    # Get the serial title
    serial = u['code']
    log(f'Serial code is [{serial}]')

    return 'search', serial


def get_actors_data(url_parts):
    star_code = url_parts['code']

    log(f'Star code is [{star_code}]')

    return 'star', star_code


data_washer = {
    'search': get_serials_title,
    'star': get_actors_data,
}

if __name__ == '__main__':
    urls = [
        'https://www.javbus.com/search/TMVR&type=&parent=ce',
        'https://www.javbus.com/star/qmc',
    ]

    for u in urls:
        url_parser(u)
