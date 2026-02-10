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
    args_list = [('A',2), ('B',3), ('C',5), ('D',4)]
    time_1 = time.perf_counter()
    task = [asyncio.create_task(call_api(name=name, delay=delay)) for name, delay in args_list]
    print('Coroutines start')

    # await asyncio.wait(task)
    await asyncio.gather(*task)

    time_2 = time.perf_counter()
    print(f'Spent {time_2 - time_1} seconds')
    print('Coroutines done')

if __name__ == '__main__':
    asyncio.run(main())
