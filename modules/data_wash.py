from pyquery import PyQuery as pq
from modules.cache import get_content
from modules import generate_coser_url
from utils import log
import json


def get_posts_list(coser_id):
    c = coser_id
    url = generate_coser_url(c)
    content = get_content(url)

    html = pq(content)
    script = html('script')
    log(type(script))
    for s in script:
        sc = pq(s)
        if sc.text().find('JSON.parse') > 0:
            log(sc.text())
            plist = get_posts(sc.text())
            # log(plist)


def get_posts(content):
    c = content
    dell = c.find('("') + 2
    delr = c.find('")')
    c = c[dell:delr]
    log(c)
    c = c.replace('\\"', '\"')
    log(c)
    obj = json.loads(c)

    for k in obj['post_data']['list']:
        log(k)
        log(k['since'])
    return obj
