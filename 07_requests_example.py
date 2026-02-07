#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/7 10:17
Email : adamyue@163.com
'''
import requests
url = 'https://www.baidu.com'
response = requests.get(url)
response.encoding = 'utf-8'
print(response.text)