import asyncio
import threading
import time
import urllib.request

import aiohttp

urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org'] * 10

async def call_url(url):
    response = await aiohttp.get(url)
    data = await response.text()
    return data

futures = [call_url(url) for url in urls]

loop = asyncio.get_event_loop()
t0 = time.time()
loop.run_until_complete(asyncio.wait(futures))

print(time.time() - t0)


def call_url(url):

    resp = urllib.request.urlopen(url)

    return resp.read()

threads = [threading.Thread(target=call_url, args=(url,)) for url in urls]

t0 = time.time()
for t in threads:
    t.start()

for t in threads:
    t.join()

print(time.time() - t0)
