import asyncio
import time

import requests
import aiohttp


async def get_url_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


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

    print("[*] Sync Requests Took: ", end_time - start_time)

    start_time = time.time()
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url_response(url)))

    async_text_response = await asyncio.gather(*tasks)

    end_time = time.time()

    print("[*] Async Requests Took: ", end_time - start_time)

    """ 
    >> Result
    
    [*] Sync Requests Took:  8.698022603988647
    [*] Async Requests Took:  1.975555658340454
    """


if __name__ == '__main__':
    # Run on One Core
    # we need event loop to run the loop
    asyncio.run(main())
