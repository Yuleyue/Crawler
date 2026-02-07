#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/7 9:14
Email : adamyue@163.com
'''
from urllib.request import urlopen
url = 'http://www.baidu.com'
response = urlopen(url)
# print(response.read().decode('utf-8'))
with open('baidu.html','w', encoding='utf-8') as f:
    f.write(response.read().decode('utf-8'))
