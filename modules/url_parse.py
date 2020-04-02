from utils import log


def url_parser(url_parsing):
    """
    Confirm url kind and start the washer
    :param url_parsing: url
    """

    # find which the url kind
    url_part_list = url_parsing.split('/')
    spider_type = url_part_list[-2]

    log(spider_type)

    data_washer[spider_type](url, url_part_list)

    return 0


def get_serials_title(url_raw, url_part_list):
    url_tail = url_part_list[-1]

    # Get the serial title
    serial = url_tail.split('&')[0]
    log(serial)


def get_actors_data(url_raw, url_part_list):
    log(url_part_list[-2])


data_washer = {
    'search': get_serials_title,
    'star': get_actors_data,
}

if __name__ == '__main__':
    url = [
        'https://www.javbus.com/search/avvr&type=&parent=ce',
        'https://www.javbus.com/star/qmc',
    ]

    for u in url:
        url_parser(u)
