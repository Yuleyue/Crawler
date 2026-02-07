#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/7 10:42
Email : adamyue@163.com
'''
# requests.post 响应取值方法
# 经查阅资料，发现requests库 ，res.text返回的是decode处理后的Unicode型的数据，r.content 返回的是bytes 二进制的原始数据。
# \u表示的那一 串unicode编码
# print(res.text.encode().decode("unicode_escape"))
# 如果需要原始文本，可用 response.text；二进制数据用 response.content。
# 对于复杂 JSON，建议先 print(response.json()) 查看结构，再按层级取值。

import requests

url = 'https://fanyi.baidu.com/sug'
data = {
    'kw': 'apple',
    # 'kw': input('Input your word: '),
}
res = requests.post(url, data=data)
print('content converting: ')
bytes_con = res.content
# res.content 返回的是bytes 二进制的原始数据
print('1. binary content: ')
print(bytes_con)
print('2. decoding bytes content to unicode: ')
print(bytes_con.decode(encoding="unicode_escape"))
print('---' * 30)

print('original text: ')
print('1. encoding: ')
# res.text返回的是decode处理后的Unicode型的数据
print('res.text返回的是decode处理后的Unicode型的数据')
print(res.text)
print('2. decoding unicode: ')
# r.encoding = r.apparent_encoding
# print(res.apparent_encoding)
print(res.text.encode(res.apparent_encoding).decode("unicode_escape"))
print('---' * 30)

print('json dict: ')
print(res.json())
