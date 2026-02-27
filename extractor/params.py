from urllib.parse import urlparse, parse_qs

def extract_params(url):
    parsed = urlparse(url)
    return list(parse_qs(parsed.query).keys())
