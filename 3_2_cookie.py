#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/8 20:25
Email : adamyue@163.com
'''
import requests

# TODO: get contId      contId=1805024
url = 'https://www.pearvideo.com/video_1805024'
contId = url.split('_')[1]

# TODO: get json returned by videoStatus, then the srcURL
videoStatusUrl = f'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.2671959239797347'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
    'Referer': url      # Hotlinking protection
}
response = requests.get(videoStatusUrl, headers=headers)
# print(response.text)
# TODO: adjust srcURL
# srcUrl:       https://video.pearvideo.com/mp4/short/20260205/1770554923422-16072077-hd.mp4
# Real addr:    https://video.pearvideo.com/mp4/short/20260205/cont-1805024-16072077-hd.mp4
dic = response.json()
systemTime = dic['systemTime']
srcUrl = dic['videoInfo']['videos']['srcUrl']
srcUrl = srcUrl.replace(systemTime, f'cont-{contId}')
# TODO: download the right video
with open('dl_mp4.mp4', 'wb') as f:
    f.write(requests.get(srcUrl, headers=headers).content)
response.close()
print('>>>Done!')

