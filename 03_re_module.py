#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/7 20:03
Email : adamyue@163.com
'''
import re

s='''
<div class="container"><span id='10086'>中国移动</span></div>
<div class="container"><span id='10010'>中国联通</span></div>
'''
reg = re.compile(r"<span id='(?P<id>\d+)'>(?P<name>.*?)</span>")
result = reg.finditer(s)
for item in result:
    id = item.group('id')
    name = item.group('name')
    print(id, name)