#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/7 21:56
Email : adamyue@163.com
'''

import re
import requests

# TODO: get address of each film
url = 'https://www.dytt8899.com/'
response = requests.get(url)
response.encoding = 'gbk'
regEx1 = re.compile(r'2026必看热片.*?<ul>(?P<block>.*?)</ul>', re.S)
result1 = regEx1.search(response.text)
if not result1:
    raise Exception('Cannot get the specified block')
concerned_block = result1.group('block')
# print(concerned_block)
regEx2 = re.compile(r"<li><a href='(?P<href_desired>.*?)' title")
result2 = regEx2.finditer(concerned_block)

regEx3 = re.compile(r'<div id="Zoom">.*?◎片　　名　(?P<movie>.*?)<br />.*?<td style="WORD-WRAP: '
                    r'break-word" bgcolor="#fdfddf"><a href="(?P<dl_addr>.*?)">', re.DOTALL)
for result in result2:
    # print(result.group('href_desired'))
    child_url = url.rstrip('/') + result.group('href_desired')
    child_response = requests.get(child_url)
    child_response.encoding = 'gbk'
    result3 = regEx3.search(child_response.text)
    movie = result3.group('movie')
    dl_addr = result3.group('dl_addr')
    print(movie, dl_addr)

# TODO: visit sub-page and extract name and download addr of the just film
