from bs4 import BeautifulSoup

from utils.url_utils import normalize_url, is_in_scope
from extractor.forms import extract_forms
from extractor.params import extract_params
from extractor.js import extract_js_endpoints


class Crawler:
    def __init__(self, base_url, fetcher, writer, max_depth=2, verbose=False):
        self.base = base_url
        self.fetcher = fetcher
        self.writer = writer
        self.visited = set()
        self.max_depth = max_depth
        self.verbose = verbose

    async def crawl(self, session, url, depth=0):
        if url in self.visited or depth > self.max_depth:
            return

        self.visited.add(url)

        html, status = await self.fetcher.fetch(session, url)

        if not html:
            return

        if self.verbose:
            print(f"[CRAWL] Depth {depth} -> {url} (Status: {status})")

        soup = BeautifulSoup(html, "html.parser")

        forms = extract_forms(soup)
        params = extract_params(url)

        if self.verbose and forms:
            print(f"[FORMS] Found {len(forms)} forms on {url}")

        if self.verbose and params:
            print(f"[PARAMS] {params} on {url}")

        record = {
            "url": url,
            "status": status,
            "params": params,
            "forms": forms,
            "depth": depth
        }

        self.writer.add(record)

        # JS extraction
        for script in soup.find_all("script", src=True):
            js_url = normalize_url(self.base, script["src"])

            js_text, _ = await self.fetcher.fetch(session, js_url)
            endpoints = extract_js_endpoints(js_text)

            for ep in endpoints:
                full = normalize_url(self.base, ep)

                if is_in_scope(self.base, full):
                    if self.verbose:
                        print(f"[JS-ENDPOINT] {full}")

                    await self.crawl(session, full, depth + 1)

        # Link crawling
        for link in soup.find_all("a", href=True):
            next_url = normalize_url(self.base, link["href"])

            if is_in_scope(self.base, next_url):
                if self.verbose:
                    print(f"[DISCOVERED] {next_url}")

                await self.crawl(session, next_url, depth + 1)
