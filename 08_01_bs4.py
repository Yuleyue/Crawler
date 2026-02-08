#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/8 9:14
Email : adamyue@163.com
'''
import requests
from bs4 import BeautifulSoup

# TODO: open the url of baishazhoudashichang
url = 'http://www.whbsz.com.cn/'
response = requests.get(url)
page = BeautifulSoup(response.text, 'html.parser')
table = page.find('td', attrs={'id': 'PriceShuCai1'}).find('table')
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    name = tds[0].text
    scale = tds[1].text
    price_high = tds[2].text
    price_low = tds[3].text
    price_mean = tds[4].text
    print(f'|{name: <20}|{scale: <20}|{price_high: >10}|{price_low: >10}|{price_mean: >10}')

table = page.find('td', attrs={'id': 'PriceShuiChan1'}).find('table')
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    name = tds[0].text
    scale = tds[1].text
    price_high = tds[2].text
    price_low = tds[3].text
    price_mean = tds[4].text
    print(f'{name: <30}\t{scale: <30}\t{price_high: >15}\t{price_low: >15}\t{price_mean: >15}')