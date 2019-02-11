from pyquery import PyQuery as pq
from modules.cache import get_content
from modules import generate_coser_url
from utils import log


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
            log(plist)


def get_posts(content):
    c = content
    delr = c.find('("')
    c = c[:delr]


