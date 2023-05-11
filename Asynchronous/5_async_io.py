import asyncio
import time

import requests


async def main():
    urls = [
        'https://google.com',
        'https://wikipedia.org/wiki/concurrency',
        'https://python.org',
        'https://pypi.org/projects/requests/',
        'https://docs.python.org/3/library/asyncio-task.html',
        'https://www.apple.com',
        'https://medium.com',
    ]

    start_time = time.time()
    sync_text_response = []
    for url in urls:
        sync_text_response.append(requests.get(url).text)
    end_time = time.time()

    print("[*] Requests Took: ", end_time - start_time)


if __name__ == '__main__':
    # Run on One Core
    # we need event loop to run the loop
    asyncio.run(main())
