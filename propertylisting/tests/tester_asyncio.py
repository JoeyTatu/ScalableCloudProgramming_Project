import asyncio
import aiohttp
import requests

from timer import timer

URL = 'https://httpbin.org/uuid'


async def fetch(session, url):
    async with session.get(url) as response:
        json_response = await response.json()
        print(json_response['uuid'])


# @timer(1, 1)
async def main():
    async with aiohttp.ClientSession() as session:
        #   create a list of code routines
        tasks = [fetch(session, URL) for _ in range(100)]  # list of arguments
        await asyncio.gather(*tasks)     # * converts list to args


@timer(1, 5)
def func():
    asyncio.run(main())
