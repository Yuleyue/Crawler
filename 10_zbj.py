#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/8 15:48
Email : adamyue@163.com
'''
# import requests
# from lxml import etree
#
# url = 'https://www.zbj.com/fw/?k=saas'
# res = requests.get(url)
# res.encoding = 'utf-8'
# print(res.text)
#
# et = etree.HTML(res.text)

"""
1. 拿到页面源代码
2. 从页面源代码中提取你需要的数据，价格，名称，公司名称
"""
import requests
from lxml import etree

url = "https://beijing.zbj.com/search/f/?type=new&kw=saas&r=2"
resp = requests.get(url)
resp.encoding = "utf-8"
# print(resp.text)

# /html/body/div[2]/div/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]
# 提取数据
et = etree.HTML(resp.text)
# divs = et.xpath("//div[@class='search-result-list-service search-result-list-service-width']/div")
divs = et.xpath("/html/body/div[2]/div/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[3]/div[1]")

if divs:
    print('Effective')

for div in divs:
    # 此时的div就是一条数据，对应一个商品信息
    # price = div.xpath("./div/div[2]/div[1]/span/text()") # 这里存在一个问题就是第一个和第二个取的时候存在差异，可以用下面的语句解决
    # 商品价格
    price = div.xpath("./div//div[@class='bot-content']/div[1]/span/text()")[0]
    # 服务名称
    serve_name = "_".join(div.xpath("./div//div[@class='bot-content']/div[2]/a/text()"))
    # 售出数量
    sale_num = div.xpath("./div/div[@class='bot-content']/div[4]/div[2]/div/span[2]/text()")[0]
    # 公司名称
    company = div.xpath("./div/a/div[2]/div/div/text()")[0]
    print(company, serve_name, price, sale_num)

