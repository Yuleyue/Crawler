#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/7 20:23
Email : adamyue@163.com
'''

import requests, re

with open('doubanTop250.csv', 'w', encoding='utf-8') as f:
    # TODO: get the original code
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0'}
    regEx = re.compile(r'<div class="item">.*?<span class="title">(?P<film_name>.*?)</span>'
                       r'.*?<p>.*?导演: (?P<director>.*?)&nbsp;.*?<br>'
                       r'(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">'
                       r'(?P<score>.*?)</span>.*?<span>(?P<people>.*?)人评价</span>', re.DOTALL)

    for i in range(0,250,25):
        print(f'>>> from {i + 1} to {i + 25}')

        url = 'https://movie.douban.com/top250?start='+str(i)
        response = requests.get(url, headers=header)
        pageSoure = response.text

        # TODO: compile regex, extract data
        result = regEx.finditer(pageSoure)

        # TODO: save the right datum

        for match in result:
            film_name = match.group('film_name')
            director = match.group('director')
            year = match.group('year').strip()
            score = match.group('score')
            people = match.group('people')
            f.write(f'{film_name},{director},{year},{score},{people}\n')

        response.close()

print('>>> Done!')
