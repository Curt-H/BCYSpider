from pyquery import PyQuery as pq
from modules.cache import get_content
from modules import generate_coser_url, generate_post_url
from model.posts import Post
from utils import log
from html import unescape
import json


def get_posts_list(coser_id):
    """
    wash the coser's all post page and
    split the posts information out
    :param coser_id: STRING
    :return: LIST of post objectives
    """
    plist = list()
    c = coser_id
    url = generate_coser_url(c)
    content = get_content(url)

    # initialize the PyQuery object
    html = pq(content)
    # Get the content inside <script> labels
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


def save_pics_from_each_post(postlist, sleeptime=3):
    """

    :param postlist: list, contains all coser posts obj
    :return: state code
    """
    pl = postlist

    for p in pl:
        log(p.url)
        content = get_content(p.url)
        get_pics_from_json(content)


def get_pics_from_json(content):
    """
    parse content and return the pics list
    :param content: STRING html content of post page
    :return: LIST contains the pics of post
    """
    c = content
    posts = list()

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
    log(f'Get json string\n{c}')
    posts_info = json.loads(c)
    pics = posts_info['detail']['post_data']['multi']
    log(posts_info['detail']['post_data']['multi'])
    for p in pics:
        log(p['original_path'])
    return 0
