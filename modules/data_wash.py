from pyquery import PyQuery as pq
from modules.cache import get_content
from modules import generate_coser_url, generate_post_url
from model.posts import Post
from utils import log
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
    # remove the transfer symbol
    c = c.replace('\\"', '\"')
    log(f'Get json string\n{c}')
    posts_info = json.loads(c)

    for k in posts_info['post_data']['list']:
        data = dict(
            id=k['since'],
            url=generate_post_url(k['since']),
            coser=k['item_detail']['uname'],
            cid=k['item_detail']['uid'],
            description=k['item_detail']['plain'],
        )

        post = Post(data)
        posts.append(post)
        log(post)

    log(len(posts))
    return posts_info
