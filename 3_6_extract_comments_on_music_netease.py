#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/9 14:31
Email : adamyue@163.com
'''
import base64
import requests, json
from Crypto.Cipher import AES

# TODO: Get url
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token=734a29744512d9f0252e6f6dc7e6f388'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0',
    'Referer': 'https://music.163.com/song?id=2757569265'
}



# 明文参数与密钥，须从浏览器中跟踪html文件得到
plain_data = {
    'csrf_token': "734a29744512d9f0252e6f6dc7e6f388",
    'cursor': "-1",
    'offset': "0",
    'orderType': "1",
    'pageNo': "3",
    'pageSize': "20",
    'rid': "R_SO_4_2757569265",
    'threadId': "R_SO_4_2757569265"
}

# TODO: encrypt
'''
function a(a) {         # generate a 16-bytes random string composed by digital and alphabetic characters
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)          # b->secKey
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")     # d->offset
          , e = CryptoJS.enc.Utf8.parse(a)          # a->plaintext
          , f = CryptoJS.AES.encrypt(e, c, {        # e->plaintext, c->secKey
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {            # d->plain_data, e->bod1x(["流泪", "强"]), f->bod1x(AY2x.md), g->bod1x(["爱心", "女孩", "惊恐", "大笑"])
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
    window.asrsea = d
    
         refer:           d                           e               f                               g
#   window.asrsea(JSON.stringify(i6c), bod1x(["流泪", "强"]), bod1x(AY2x.md), bod1x(["爱心", "女孩", "惊恐", "大笑"]));
'''

# args e - g
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = 'IqiQ1Z6rOvsE3AGq'

'''
# 固定i后，加密得到的参数与密钥
params=9CAbb6OF1PNHiRtTQtjVBZU71Bloe2S4rFzSvgMPS1YefBcvZKS34MdTGHPd1SWyVdblKU0OcG88jzBxoPamNE7se2jwSbIHEww%2Bs90rGuw9v4rw%2FFyFJq1bmdey1uEZ0%2Bv%2FgPuIexue4UUxcSnFwQTJILk%2FIktq6KEsQ30rQnpcpjjDbJHSh7PJlGdMmDGIiZ5f8c9ahMjdaUX5mIwHcLPfqn%2BmucIWVFRYgeZ8yqZiHEGKOuJs3LUB%2FhBJP%2B9HfDGWDViL4BDDlyZn56WtYfU0D%2B3oQxTmVloNIRoi%2BOHHb8Moy4pF8MwI6z6SOgnJ4PcXD%2BInIX2uyecVvkUsZOf4p6u1zsMmeQLAZssrJso%3D&encSecKey=7bbf93b2d79ef603519b6ab8c74500fff8993ccca7abf4669fc0c76bc18a9f5b997eab7ef24e566fa472b1b683986f7e4c8dffb6cca5bf7d8c61ffc40699581d8e6c8ee8d31de9fd75586b4581ee8411f93e06018c170ba9e9c827b4a87eeba5466704cf81b18f00ba630cea9891acebf12a5d0d4b9440f5e6c8874821d8f2bc
'''
def get_encSecKey():            # 当i定死后，h.encSecKey = c(i, e, f)生成的encSecKey也是定值了
    return '7bbf93b2d79ef603519b6ab8c74500fff8993ccca7abf4669fc0c76bc18a9f5b997eab7ef24e566fa472b1b683986f7e4c8dffb6cca5bf7d8c61ffc40699581d8e6c8ee8d31de9fd75586b4581ee8411f93e06018c170ba9e9c827b4a87eeba5466704cf81b18f00ba630cea9891acebf12a5d0d4b9440f5e6c8874821d8f2bc'

def get_params(data):
    res = enc_params(data, g)
    res = enc_params(res, i)
    return res

def padding(data):
    pad = 16 - len(data) % 16
    return data + chr(pad) * pad

def enc_params(data, encSecKey):
    iv = "0102030405060708"
    data = padding(data)
    aes = AES.new(key=encSecKey.encode('utf-8'), mode=AES.MODE_CBC, iv=iv.encode('utf-8'))
    bs = aes.encrypt(data.encode('utf-8'))
    b64encoded = base64.b64encode(bs).decode('utf-8')
    return b64encoded

if __name__ == '__main__':
    response = requests.post(url, data={
        'params': get_params(json.dumps(plain_data)),
        'encSecKey': get_encSecKey()
    })

    print(response.text)

