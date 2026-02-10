#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/10 10:15
Email : adamyue@163.com
'''
import asyncio

import aiofiles
import aiohttp

# TODO: Given a url list storing pics-url
urls = [
    'https://oss-img.mengguzhiai.com/tutuji/20240604/hrxhsz2btbj.jpg',
    'https://oss-img.mengguzhiai.com/tutuji/20240604/1pwqva1mwrg.jpg',
    'https://oss-img.mengguzhiai.com/tutuji/20240604/gut4qzo0vy3.jpg'
]

# TODO: async operation call
async def aio_download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            async with aiofiles.open(url.split('/')[-1], 'wb') as f:
                await f.write(await resp.content.read())

    print(f'>>>Downloading {url.split("/")[-1]} completed!')

async def main():
    tasks = [asyncio.create_task(aio_download(url)) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
    print('>>>All Done!')