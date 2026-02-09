#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/9 22:14
Email : adamyue@163.com
'''
import time
from concurrent.futures import ThreadPoolExecutor

def task(name: str):
    print(f'{name} - step 1\n', end='')
    time.sleep(1)
    print(f'{name} - step 2\n', end='')

    return f'{name} - completed'

with ThreadPoolExecutor() as executor:
    result_1 = executor.submit(task, 'A')
    result_2 = executor.submit(task, 'B')
    print(result_1.result())
    print(result_2.result())

with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(task, ['C', 'D'])
    for result in results:
        print(result)

