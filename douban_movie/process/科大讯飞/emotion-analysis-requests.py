# -*- coding: UTF-8 -*-
import time
import urllib.request
import urllib.parse
import json
import hashlib
import base64
import pandas as pd
# 接口地址
url = "http://ltpapi.xfyun.cn/v2/sa"
# 开放平台应用ID
x_appid = "472832d9"
# 开放平台应用接口秘钥
api_key = "6d82c3a23780f8e64cc4e3b42b28fd4f"
# 语言文本
TEXT = "汉皇重色思倾国，御宇多年求不得。杨家有女初长成，养在深闺人未识。天生丽质难自弃，一朝选在君王侧。"


def make_request(comment, savePath):
    print("---------------------------------------------------")
    print("评论文本：")
    print("    " + comment)
    print("\n评论观点：")
    body = urllib.parse.urlencode({'text': comment}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(
        param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode(
        'utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    # print(result.decode('utf-8'))
    data = json.loads(result.decode('utf-8'))
    item = data['data']
    item['comment'] = comment
    print(item)
    df = pd.DataFrame([item], columns=['comment', 'score', 'sentiment'])
    df.to_csv(savePath, index=False, mode='a', header=None)
    time.sleep(0.5)


def read_data(ReadPath, savePath):
    df = pd.read_csv(ReadPath, sep='\t')
    for comment in df.content:
        make_request(comment, savePath)


if __name__ == '__main__':
    # read_data('./data/导演创作(13948).csv', './data/analysis/导演创作.csv')
    read_data('./data/后期制作(14347).csv', './data/analysis/后期制作.csv')
