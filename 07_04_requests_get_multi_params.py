#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/7 15:47
Email : adamyue@163.com
'''

import requests

url= 'https://movie.douban.com/j/chart/top_list'

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'}

data = {
    'type': '13',
    'interval_id':'100:90',
    'action':'',
    'start':'0',
    'limit':'20'
}

res = requests.get(url, headers=headers, params=data)
print(res.text)
print(res.request.url)