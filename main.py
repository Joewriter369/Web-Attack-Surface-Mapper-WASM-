import argparse
import asyncio
import aiohttp
from collections import Counter

from core.crawler import Crawler
from core.fetcher import Fetcher
from storage.writer import Writer


def banner():
    print("""
=========================================
 Web Attack Surface Mapper (WASM)
=========================================
	@VNONYMOUS
""")


def summary(data):
    urls = len(data)
    forms = sum(len(r["forms"]) for r in data)
    params = sum(len(r["params"]) for r in data)

    statuses = Counter([r["status"] for r in data])

    print("\n========== SCAN SUMMARY ==========")
    print(f"Total URLs Crawled     : {urls}")
    print(f"Total Forms Found      : {forms}")
    print(f"Total Parameters Found : {params}")
    print("\nStatus Code Distribution:")
    for k, v in statuses.items():
        print(f"  {k} → {v}")
    print("==================================\n")


async def run(args):
    fetcher = Fetcher(rate_limit=args.rate, verbose=args.verbose)
    writer = Writer(args.output, verbose=args.verbose)

    crawler = Crawler(
        base_url=args.url,
        fetcher=fetcher,
        writer=writer,
        max_depth=args.depth,
        verbose=args.verbose
    )

    async with aiohttp.ClientSession() as session:
        await crawler.crawl(session, args.url)

    writer.save()
    summary(writer.data)


def main():
    parser = argparse.ArgumentParser(
        prog="wasm",
        description="Async Web Crawler & Attack Surface Mapper",
        epilog="""
Examples:
  wasm -u https://example.com
  wasm -u https://target.com -d 3 -r 10 -o out.json --verbose
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "-u", "--url",
        required=True,
        help="Target base URL (e.g. https://example.com)"
    )

    parser.add_argument(
        "-d", "--depth",
        type=int,
        default=2,
        help="Crawl depth (default: 2)"
    )

    parser.add_argument(
        "-r", "--rate",
        type=int,
        default=5,
        help="Concurrent request limit (default: 5)"
    )

    parser.add_argument(
        "-o", "--output",
        default="output.json",
        help="Output JSON file (default: output.json)"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output (debug mode)"
    )

    args = parser.parse_args()

    banner()
    asyncio.run(run(args))


if __name__ == "__main__":
    main()
