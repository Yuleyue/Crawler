#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/8 22:47
Email : adamyue@163.com
'''
import json

import requests
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

'''
params
L6SZRK81hT188lF2gQVI5bhhvC+aZAxKN0CH20s/lmOBvDNuSanvVwLxGKr0o0yrytj3SlcQh1jYpZMJRel0MgpiT6G2ZvDpMuedC/BD9v33NT/8P/lwdrgcM8Wkwdiqc49pX90Y+PnzjWlmfyz8N6xTT1fTjZIpHK3CCu+vx0pOYWodMSRvnp48DCFs0sAOlBzkid6Wy2id9m4+KNEGhevLh889JeM8Y6EZhm4otz7MiI4jnB1PhKZR6zoH+tbHiFofAsQznKQIkdZ/zz05x47CapFQgem4qLufMhrr9ZKVYscjSjyIUjSoD+eunnPK
encSecKey
a7ae5b0608f71afd8374f377cc712cb8650e5515f5aa4bb5749d87d9d0b06843fe75027cc6fa7abf6d1c0974c2fd232faee15a4bafdd208424307b41904da0ebf93b1107ed9938c9c332151b9ef2f7db80ebcb444ae288276fa4dc8c41825aba5688ab08e52afff2aa17b295b9c7c9371563f7c344b4bb3bc08c3817f8973565

params=1x4HMJj5xmumf4gJvFLNAIS9Ey4d6zIPY1neh0ZMVZqOD3UZS3PrHULtgr8gmGTxHqCrqs10C0aQCfgevTnkBVebwqkwDjD%2FNtnRSi60POrxxzgwiXhvNgl9Nnidf2Mg0A6NKx5HhxJO0R%2B5jihUx6PVOV6vGKXfuwvYbI9twcH16f64u07gwdF3ouTmp0pVatgV4arfQ3cgoPCOkhAD18qjAL7EE5f%2B1%2Bp%2BW4UculijCAmo3vfLjdbrHxhUmvZbTYokjwt3HC%2BdkoL9dRmLHXMx4BQkMymlOxHXy6b6HByonS8OM1jMMj2Er7qRc%2BUm2%2Bzcr%2B5rnxM0f%2Fd9BrGxyPGNw1dahl8MVcGnSEI%2BrhY%3D&encSecKey=91dee48f52a60ab98c739a34e16e254c9d897055d9e77ec9c510f6d60ff35028e9823659196eae6082fa7808e4a38f458a5928cd2450be31b45d212cf851b3f848a6182744811ae6cfd37e84eb0355c460c3b40e2fab3107ec8893e83f91159d28bebc80ada6ac6eef34faa2d98109bedaf3f81bc92c1d026b395976731225ab
https://music.163.com/weapi/comment/resource/comments/get?csrf_token=734a29744512d9f0252e6f6dc7e6f388
'''
'''
    function a(a) { # a = 16
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)          # loop 16 times
            e = Math.random() * b.length,   # generate a random number in (0, 62)
            e = Math.floor(e),              # 取整
            c += b.charAt(e);               # 在b中取16个随机字符存入c中，即生成的c为一个长度为16的由数字与字母组成的字符串
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)              # 是 CryptoJS 库中用于将字符串转换为 WordArray 对象的方法。它通常用于加密操作中，将明文字符串转换为适合加密算法处理的格式
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {            # 明文、密钥
        iv: d,                                          # 偏移量
            mode: CryptoJS.mode.CBC
        });
        return f.toString()                             # 返回加密后的字符串
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {    # d: data, e, f, g: saved as below
        var h = {}              # 空字符串
          , i = a(16);          # i是长为16位的由字母与数字组成的随机字符串
        return h.encText = b(d, g),     # d是数据，g是密钥
        h.encText = b(h.encText, i),    # h.encText是数据，i是密钥，返回的就是params
        h.encSecKey = c(i, e, f),       # 返回的是encSecKey
        h
    }

'''

# TODO: get params without encryption
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token=734a29744512d9f0252e6f6dc7e6f388'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
    'Referer': 'https://music.163.com/song?id=3345641707'
}

data = {
    'csrf_token': "734a29744512d9f0252e6f6dc7e6f388",
    'cursor': "-1",
    'offset': "0",
    'orderType': "1",
    'pageNo': "1",
    'pageSize': "20",
    'rid': "R_SO_4_3345641707",
    'threadId': "R_SO_4_3345641707"
}
# TODO: encrypting params according to netease, gen encSecKey
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = "hfoUInLaZrfPOwFe"


def get_encSecKey():
    # Generating encSecKey according to the specified fixed i
    return '6e10c06c88bb080fba3587dc258222fdc28fb52f481baadda805f98ac1ec27c1d77cbc817d582c71f0cd25fc6afbc6b45dcedb9b1f8e317821bec7a88127a3f3f2810ebddc9c327d47d00dec3370a0c830958ec29acf3d2c60a43e98e17362561579c0cec6ce9ac9a353f080dd8e0ec5bf8d5097ab15b14f59a8e98853d7dac7'


def get_params(data):  # default, data is string
    res = enc_params(data, g)
    res = enc_params(res, i)
    return res


'''
key(bytes/ bytearray/ memoryview): The secret key to use in the symmetric cipher.  
It must be 16 (*AES-128)*, 24 (*AES-192*) or 32 (*AES-256*) bytes long.
'''


def to_16_multiple(data: str):
    pad = 16 - len(data) % 16
    data += chr(pad) * pad
    return data


def enc_params(plaintext: object, key: object) -> object:  # encryptor
    iv = "0102030405060708"
    plaintext = to_16_multiple(plaintext)
    aes = AES.new(key=key.encode('utf-8'), mode=AES.MODE_CBC, IV=iv.encode('utf-8'))
    bs = aes.encrypt(plaintext.encode('UTF-8'))
    return b64encode(bs).decode('utf-8')


# TODO: request netease web, get comments
resp = requests.post(url, headers=headers, data={
    'params': get_params(json.dumps(data)),
    'encSecKey': get_encSecKey(),
})
print(resp.text)
