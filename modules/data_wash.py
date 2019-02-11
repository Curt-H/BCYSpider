from pyquery import PyQuery as pq
from modules.cache import get_content
from modules import generate_coser_url


def get_posts_list(coser_id):
    c = coser_id
    url = generate_coser_url(c)
    content = get_content(url)

    html = pq(content)
    print(html)
