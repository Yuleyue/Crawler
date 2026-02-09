#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/10 6:43
Email : adamyue@163.com
'''
import asyncio


async def calc(n1: int, n2: int) -> int:
    res = n1 + n2
    print(res)

async def main():
    print('main - step 1')
    await calc(1, 2)
    print('main - step 2')

asyncio.run(main())