#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/11 19:31
Email : adamyue@163.com
'''
import json

import requests

'''
1、从源代码中找到指向影视源的M3U8文件的链接信息
'''
'''
如，第一集，从网页检查元素追踪到如下链接：
https://play.modujx14.com/20240803/lQH9oMP2/index.m3u8
接下来，应从入口网页https://www.92zhuiju.cc/vod/play/id/53577/sid/1/nid/1.html处，通过对网页源代码的追踪，找到上述信息的蛛丝马迹
https://www.92zhuiju.cc/jiexi/?url=https://play.modujx14.com/20240803/lQH9oMP2/index.m3u8
'''

url = 'https://www.92zhuiju.cc/vod/play/id/53577/sid/1/nid/1.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print(response.text)
