import asyncio
import os.path
import re

import aiofiles
import aiohttp
import requests

# 生成目录存储下载文件
if not os.path.exists('./ts_files'):
    os.makedirs('./ts_files')

url = 'https://bizapi.csdn.net/edu-academy-web/v1/material/info?materialId=638733&courseId=39353&cId=39353&playerVersion=2&isFree=2&isMember=2'

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'uuid_tt_dd=10_19729521400-1768134937663-957549; fid=20_18601423211-1768134935730-442379; loginbox_strategy=%7B%22blog-threeH-dialog-exp11tipShowTimes%22%3A1%2C%22blog-threeH-dialog-exp11%22%3A1769908152960%7D; UserName=Yuleyue; UserInfo=f2006b77e4224753b09da3771587823f; UserToken=f2006b77e4224753b09da3771587823f; UserNick=Yuleyue; AU=5D6; UN=Yuleyue; BT=1769908291847; p_uid=U010000; csdn_newcert_Yuleyue=1; c_dl_um=-; _clck=191sth9%5E2%5Eg3h%5E0%5E2202; c_dl_prid=1770021202755_944026; c_dl_rid=1770852203196_543339; c_dl_fref=https://blog.csdn.net/u010865136/article/details/90401889; c_dl_fpage=/download/qq_25111607/8386755; __gads=ID=8955d2d90a44978c:T=1768134939:RT=1770852734:S=ALNI_Mayu4It7d_OFnizc-o7qmdzrUf8ag; __gpi=UID=000011e25f5684d4:T=1768134939:RT=1770852734:S=ALNI_MaFDlUrDu4M4Uwrh6IANtW7EJW3kQ; __eoi=ID=4099b35488a493e7:T=1768134939:RT=1770852734:S=AA-AfjZkvBHCNgrjKYkqkevhZg--; _clsk=zu2u80%5E1770852735505%5E4%5E0%5El.clarity.ms%2Fcollect; dc_session_id=10_1770881841503.502358; c_pref=default; c_ref=default; c_first_ref=default; c_first_page=https%3A//edu.csdn.net/learn/39353/638733%3Fspm%3D3001.4143; c_segment=13; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1770507567,1770610849,1770733461,1770881842; HMACCOUNT=43FBC1F66C38775C; dc_sid=71af32c334eca1a2eeb3ddb4dc2d6a08; c_dsid=11_1770882341308.387401; c_page_id=default; dc_tos=tac5k5; log_Id_pv=4; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1770882342; log_Id_view=7',
    'origin': 'https://edu.csdn.net',
    'priority': 'u=1, i',
    'referer': 'https://edu.csdn.net/learn/39353/638733?spm=3001.4143',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Microsoft Edge";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
    'x-ca-key': '203866374',
    'x-ca-nonce': 'b217a4a1-327c-43b8-bec7-c882ffdd0822',
    'x-ca-signature': 'perpu9WdLnsbNhrfwfTTVbdz2gqyu9blArvlwvbKt2g=',
    'x-ca-signature-headers': 'x-ca-key,x-ca-nonce'
}

def get_first_level(url: str, headers: dict) -> dict:
    response = requests.get(url, headers=headers)
    return response.json()

def get_title(json_data: dict) -> str:
    title = json_data['data']['title']
    return title

def get_m3u8_url(json_data: dict) -> str:
    m3u8_url = json_data['data']['info']['playUrl']
    return m3u8_url

def get_ts_url_lst(m3u8_url: str, headers: dict) -> list:
    m3u8 = requests.get(m3u8_url, headers=headers).text
    ts_lst = re.findall(r',\n(.*?)\n#', m3u8)
    pre_url = m3u8_url.split('play_video')[0]
    ts_url_lst = list()
    for ts in ts_lst:
        ts_url = pre_url + 'play_video/' + ts
        ts_url_lst.append(ts_url)

    return ts_url_lst

# 下载ts文件
async def download_ts(session, url):
    async with session.get(url) as response:
        ts_name = 'ts_files/' + url.split('/')[-1]
        async with aiofiles.open(ts_name, mode='wb') as f:
            await f.write(await response.read())
            print(f'{ts_name} downloaded')

async def main():
    js_data = get_first_level(url, headers=headers)
    m3u8_url = get_m3u8_url(js_data)
    ts_url_lst = get_ts_url_lst(m3u8_url, headers)

    async with aiohttp.ClientSession() as session:
        for ts_url in ts_url_lst:
            await download_ts(session, ts_url)
            break


if __name__ == '__main__':
    asyncio.run(main())