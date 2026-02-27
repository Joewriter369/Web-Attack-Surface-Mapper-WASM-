import aiohttp
import asyncio

class Fetcher:
    def __init__(self, rate_limit=5, verbose=False):
        self.semaphore = asyncio.Semaphore(rate_limit)
        self.verbose = verbose

    async def fetch(self, session, url):
        async with self.semaphore:
            try:
                if self.verbose:
                    print(f"[FETCH] {url}")

                async with session.get(url, timeout=10) as response:
                    return await response.text(), response.status

            except Exception as e:
                if self.verbose:
                    print(f"[ERROR] {url} -> {e}")
                return "", 0
