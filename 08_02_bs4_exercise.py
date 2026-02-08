#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/8 10:40
Email : adamyue@163.com
'''
import requests
from bs4 import BeautifulSoup

url = 'https://www.umei.net/'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
img_lst = soup.find_all('img', attrs={'class': 'waitpic'})
# print(len(img_lst))
for i, img in zip(range(len(img_lst)), img_lst):
    img_url = img.get('data-original')
    img_source = requests.get(img_url)
    with open(f'Pic_{i}.jpg', 'wb') as f:
        f.write(img_source.content)