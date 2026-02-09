#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/10 6:53
Email : adamyue@163.com
'''
import asyncio
import time


async def call_api(name: str, delay: int):
    print(f'Call {name} - step 1')
    await asyncio.sleep(delay)
    print(f'Call {name} - step 2')

async def main():
    time_1 = time.perf_counter()
    print('start A coroutine')
    task_1 = asyncio.create_task(call_api('A', 2))

    print('start B coroutine')
    task_2 = asyncio.create_task(call_api('B', 2))

    await task_1
    print('end A coroutine')
    await task_2
    print('end B coroutine')


    time_2 = time.perf_counter()
    print(f'Spent {time_2 - time_1} seconds')

asyncio.run(main())
