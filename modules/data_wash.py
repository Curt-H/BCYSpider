import time

from pyquery import PyQuery as pq
from modules.cache import get_content, cache_pic
from modules import generate_coser_url, generate_post_url
from model.posts import Post
from utils import log
from html import unescape
import json


def get_posts_list(coser_id):
    """
    Collect one COSER's all posts page obj
    :param coser_id: STRING
    :return: LIST of post objectives
    """
    plist = list()
    c = coser_id
    url = generate_coser_url(c)
    content = get_content(url)

    # initialize the PyQuery object
    html = pq(content)
    log(f'[{c}]-[{url}]')
    # create PQ object
    title = html('title')
    log(f'coser post title:\n{title}')

    # Get the content inside <script> labels

    if title.text() == '半次元 banciyuan - ACG爱好者社区':
        log("No more pages")
        return 0
    script = html('script')
    log(type(script))

    # check the labels to find the label contains JSON content
    for s in script:
        sc = pq(s)
        if sc.text().find('JSON.parse') > 0:
            log(sc.text())

            plist += get_posts_from_json(sc.text())

    return plist


def get_posts_from_json(content):
    """

    :param content:
    :return:
    """
    c = content
    posts = list()

    # get the json string which contains posts information
    dell = c.find('("') + 2
    delr = c.find('")')
    c = c[dell:delr]

    # remove the escape characters
    c = c.replace('\\"', '\"')
    # log(f'Get json string\n{c}')
    posts_info = json.loads(c)

    # posts_info['post_data']['list'] contains all posts list
    for k in posts_info['post_data']['list']:
        description = k['item_detail']['plain']
        # Get description and remove escape characters
        description = description.replace('\\u002F', '/')
        # Change html escape characters
        description = unescape(description)

        data = dict(
            id=k['since'],
            url=generate_post_url(k['since']),
            coser=k['item_detail']['uname'],
            cid=k['item_detail']['uid'],
            description=description,
        )

        post = Post(data)
        posts.append(post)
        # log(post)

    log(len(posts))
    return posts


def get_pic_list_from_post(post, sleeptime=3):
    """
    parse post object and return a pic list
    :param post: list, contains all coser posts obj
    :param sleeptime: num, the sleep time between two download
    :return:
    """
    p = post

    log(p.url)
    content = get_content(p.url)
    pic_list = parse_post_from_json(content, p.id)

    for p in pic_list: log(p)

    return pic_list


def parse_post_from_json(content, post_id, dev="y"):
    """
        parse content and return the pics list
    :param content: STRING html content of post page
    :param post_id: post id
    :param dev: dev mode switch
    :return: LIST contains the pics of post
    """
    c = content
    pid = post_id

    # get the json string which contains posts information
    dell = c.find('("') + 2
    delr = c.find('")')
    c = c[dell:delr]

    # remove the escape characters
    c = c.replace('\\"', '\"')
    # remove unicode char
    c = c.replace('\\\\u002F', '/')
    c = c.replace('\\\\u003F', '\\')
    # c = c.replace('\\\\u003F', '\\')
    # log(f'Get json string\n{c}')

    # parse post string to get pics info
    posts_info = json.loads(c)
    pics = posts_info['detail']['post_data']['multi']
    log(pics)

    # collect pics info
    # for i, p in enumerate(pics):
    #     pic_list = p['original_path']
    #     log(p['original_path'])
    #     if dev == 'n':
    #         log("cached pic!")

    return []
# def parse_post_from_json(content, post_id, dev="y"):
#     """
#         parse content and return the pics list
#     :param content: STRING html content of post page
#     :param post_id: post id
#     :param dev: dev mode switch
#     :return: LIST contains the pics of post
#     """
#     c = content
#     pid = post_id
#
#     # get the json string which contains posts information
#     dell = c.find('("') + 2
#     delr = c.find('")')
#     c = c[dell:delr]
#
#     # remove the escape characters
#     c = c.replace('\\"', '\"')
#     # remove unicode char
#     c = c.replace('\\\\u002F', '/')
#     c = c.replace('\\\\u003F', '\\')
#     # c = c.replace('\\\\u003F', '\\')
#     log(f'Get json string\n{c}')
#
#     # todo: remember to remove
#
#     # parse post string to get pics info
#     posts_info = json.loads(c)
#     pics = posts_info['detail']['post_data']['multi']
#     log(posts_info['detail']['post_data']['multi'])
#
#     # collect pics info and download it
#     for i, p in enumerate(pics):
#         url = p['original_path']
#         log(p['original_path'])
#         if dev == 'n':
#             cache_pic(url, pid, i)
#             log("cached pic!")
#
#     return 0
