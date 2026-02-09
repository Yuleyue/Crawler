#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/9 8:40
Email : adamyue@163.com
'''
import requests
headers = {
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'
}
param = {
       'np':'1',
       'fltt':'1',
       'invt':'2',
       'cb':'jQuery37106298097149817923_1770597446049',
       'fs':'m:0+t:6+f:!2,m:0+t:80+f:!2,m:1+t:2+f:!2,m:1+t:23+f:!2,m:0+t:81+s:262144+f:!2',
       'fields':'f12,f13,f14,f1,f2,f4,f3,f152,f5,f6,f7,f15,f18,f16,f17,f10,f8,f9,f23',
       'fid':'f3',
       'pn':'3',
       'pz':'20',
       'po':'1',
       'dect':'1',
       'ut':'fa5fd1943c7b386f172d6893dbfba10b',
       'wbp2u':'|0|0|0|web',
       '_':'1770597446074'
}
url = ('https://push2.eastmoney.com/api/qt/clist/get')
response = requests.get(url, headers=headers, params=param)
print(response.text)