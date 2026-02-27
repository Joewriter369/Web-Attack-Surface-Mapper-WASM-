from urllib.parse import urljoin, urlparse

def normalize_url(base, link):
    return urljoin(base, link)

def is_in_scope(base, url):
    return urlparse(base).netloc == urlparse(url).netloc
