#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/7 10:17
Email : adamyue@163.com
'''
import requests
content = input('Please enter your concerned content: ')
url = f'https://www.sogou.com/web?query={content}'
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
# response = requests.get(url, headers=headers)
# response.encoding = 'utf-8'
# print(response.text)
print(response.request.headers)