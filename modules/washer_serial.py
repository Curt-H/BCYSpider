import time

from pyquery import PyQuery as pq
from utils import log


def get_items_info(task_info):
    """
    Parse the html content and get the title and number
    :param task_info: dict, contain url, html content search type and so on
    :return:
    """
    t = task_info
    result = dict()
    result['data'] = list()

    # find all the html which class is item
    content = pq(t['html'])
    items = content('.item')

    for i in items:
        i = pq(i)

        # get the title from img's attribute
        title = i('img').attr('title')
        number = i('date').text().split(' ')[0]

        # for star task you need to get the actress name
        if i('.avatar-box').text() != '':
            result['filename'] = title
            log(f'Set filename as |{title}|')
        else:
            result['data'].append('\t'.join([number, title]) + '\n')

    if 'filename' not in result.keys():
        result['filename'] = t['code']
        log(f'Filename is not specified, use |{t["code"]}| as filename')
    log(result['data'])
    return result


if __name__ == '__main__':
    log('fuck shit \t bitch\n')
    log('fuck shit \t bitch\n'.strip())
    log('fuck shit \t bitch'.strip())
    log('end')
