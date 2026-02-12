#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/10 22:22
Email : adamyue@163.com
'''

import requests, os
import asyncio, aiohttp, aiofiles
import json

'''
解构网页，获取资源所在关键位置信息：
    目录->https://dushu.baidu.com/api/pc/getCatalog?data={“book_id“:“4306063500“}    
    章节->https://dushu.baidu.com/api/pc/getChapterContent?data={“book_id“:“4306063500“,“cid“:“4306063500|1569782244“,“need_bookinfo“:1}
请求方法
GET
总体思路：
    1、同步操作：调用getCatalog取得全部章节的cid和title（仅调用一次）
    2、异步操作：调用main()下载各章节内容（完成相似功能的任务队列）
'''

# 取每单节的书名号bid和章节号cid，以生成每章节的下载链接
def getChapterUrl(bid: str, cid: str):      # get each chapter's url
    data = {
        'book_id': bid,
        'cid': f'{bid}|{cid}',
        'need_bookinfo':1
    }
    data = json.dumps(data)
    return f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'

# 以异步方式下载各章节
async def aiodownload(bid: str, cid: str, title: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(getChapterUrl(bid, cid)) as resp:
            if resp.status == 200:
                dic = await resp.json()
                # t_tmp = title.split(' ')
                # title = '_'.join(t_tmp)
                file_name = os.path.join(os.getcwd(), 'novel_dl', '_'.join(title.split(' ')) + '.txt')

                async with aiofiles.open(file=file_name, mode='w', encoding='utf-8') as f:
                    await f.write(dic['data']['novel']['content'])         # novel content
                    print(f'>>>{title} downloaded!')

# 同步方式取得全书目录及对应章节名称与章节号
def getCatalog(url: str, headers: dict):
    response = requests.get(url, headers=headers)
    dic = response.json()
    title = list()
    cid = list()
    # 遍历dic，取得目录中各章节名称title及章节号cid
    for item in dic['data']['novel']['items']:   # items: [{title: "第一回 灵根育孕源流出 心性修持大道生", price_status: "0", cid: "1569782244"},…]
        title.append(item['title'])
        cid.append(item['cid'])

    return title, cid

# 功能集合，下载全书各章节文档
async def main():
    tasks = list()
    titles, cids = getCatalog(url, headers=header)
    tasks = [asyncio.create_task(aiodownload(bid, cid, title)) for title, cid in zip(titles, cids)]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    bid = '4306063500'
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"' + bid + '"}'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
        'referer': 'https://dushu.baidu.com/pc/detail?gid=4306063500'
    }

    asyncio.run(main())
    print('>>>Done!')

