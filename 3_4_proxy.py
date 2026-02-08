#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/8 21:46
Email : adamyue@163.com
'''
import requests

url = 'http://www.baidu.com'
proxy = {
    'http': 'http://101.201.225.47:80',
    'https': 'https://101.201.225.47:80'
}
response = requests.get(url, proxies=proxy)
# response = requests.get(url)
response.encoding = 'utf-8'
print(response.text)