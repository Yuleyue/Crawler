#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/7 10:42
Email : adamyue@163.com
'''
# 将目标字符串str编写为目标二进制数据bytes类型，即为编码过程, 使用: str.encode(encoding_mode)
# 将二进制数据bytes转换为字符串，即为解码过程，使用: bytes.decode(encoding_mode)
# requests.post 响应取值方法
# 经查阅资料，发现requests库 ，res.text返回的是decode处理后的Unicode型的数据(字符串)，r.content 返回的是二进制的原始数据（bytes）。
# \u表示的那一 串unicode编码
# print(res.text.encode().decode("unicode_escape"))
# 如果需要原始文本，可用 response.text；二进制数据用 response.content。
# 对于复杂 JSON，建议先 print(response.json()) 查看结构，再按层级取值。


# '''
# 我们使用python中，遇到爬取网站情况，用到unicode编码，我们需要将它转换为中文，unicode编码转换为中文的方法有四种：使用unicode_escape 解码、使用encode()方法转换，
# 再调用bytes.decode()转换为字符串形式、 使用json.loads 解码（为json 格式）、使用eval（遇到Unicode是通过requests在网上爬取的时候）。具体内容请看本文。
# 方法一：使用unicode_escape 解码
# unicode = b'\\u4f60\\u597d'
# re = unicode.decode("unicode_escape")
# print(re)
# 返回：你好
# 方法二：使用encode()方法转换，再调用bytes.decode()转换为字符串形式
# s = r'\u4f60\u597d'
# print(s.encode().decode("unicode_escape"))
# 方法三： 使用json.loads 解码（为json 格式）
# str = '\u4eac\u4e1c\u653e\u517b\u7684\u722c\u866b'
# print json.loads('"%s"' %str)
# 方法四：使用eval（遇到Unicode是通过requests在网上爬取的时候）
# response = requests.get(url,headers=headers)
# re = eval("u"+"\'"+response.text+"\'")
# print(re)
# 以上就是小编整理的python中将unicode编码转换为中文的方法
# '''

# '''
# unicode_escape 是 Python 提供的一种编解码方式，主要用于在字符串和其 Unicode 转义序列（如 \u4f60\u597d）之间进行转换。它常用于处理包含 \uXXXX 格式的字符串，将其还原为可读文本。
# # 原始字符串包含 Unicode 转义
# s = "\\u5403\\u9e21\\u6218\\u573a"
#
# # 解码为正常文本
# decoded = s.encode('utf-8').decode('unicode_escape')
# print(decoded) # 输出: 吃鸡战场
# 这里 .encode() 将 str 转为 bytes，再用 .decode('unicode_escape') 将转义序列解析成真实字符。
# 编码与解码的核心用法
# 编码（encode） 将普通字符串转为包含 Unicode 转义的字节序列： text = "你好" encoded = text.encode('unicode_escape') print(encoded) # b'\\u4f60\\u597d'
# 解码（decode） 将包含 Unicode 转义的字节或字符串还原： raw = b'\\u4f60\\u597d' decoded = raw.decode('unicode_escape') print(decoded) # 你好
#
# 常见应用场景
# 网络请求结果处理：部分 API 返回的 JSON 中中文以 \uXXXX 存储，可用 unicode_escape 解码。
# 文件读取：读取包含 Unicode 转义的配置或日志文件时，将其转为可读文本。
# 调试与转储：在需要将文本安全地存储为源码字面量时，可用 encode('unicode_escape')。
#
# 注意事项
# 如果原始数据是 str 类型且直接包含转义符，需要先 .encode() 再 .decode('unicode_escape')。
# 对于二进制数据（bytes），可直接 .decode('unicode_escape')。
# 与 raw_unicode_escape 不同，unicode_escape 会对 \uXXXX 进行实际解析，而不是原样保留。
# 这样，你就可以灵活地在 Python 中处理 Unicode 转义与真实字符之间的转换了。
# '''


import requests

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'apple',
    # 'kw': input('Input your word: '),
}

res = requests.post(url, data=data)

print('content converting: ')
bytes_con = res.content                         # res.content 返回的是bytes类型的二进制的原始数据--unicode编码，要将它转换为中文，unicode编码转换为中文的方法有四种：使用unicode_escape 解码
print('1. binary content: ')
print(bytes_con)
print('2. decoding bytes content to unicode str: ')
print(bytes_con.decode(encoding="unicode_escape"))
print('---' * 30)

print('original text: ')
print('1. encoding: ')
print(res.text)                                 # res.text返回的是经decode处理后的Unicode型的字符串数据
print('2. decoding unicode: ')
print(res.text.encode().decode("unicode_escape"))  #
print('---' * 30)

print('json dict: ')
print(res.json())
