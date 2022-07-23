import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models
import pandas as pd
import time
def make_request(comment, savePath):
    print("---------------------------------------------------")
    print("评论文本：")
    print("    " + comment)
    print("\n评论观点：")
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
        # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
        cred = credential.Credential("AKIDFMGyVvpa8RaZKhrSu3Y2dGnEi04xhGgu", "A9GBwYYVJwOqFv8H442CMPMD172nPp3L")
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.SentimentAnalysisRequest()
        params = {
            "Text": str(comment)
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个SentimentAnalysisResponse的实例，与请求对象对应
        resp = client.SentimentAnalysis(req)
        # 输出json格式的字符串回包
        item = json.loads(resp.to_json_string())
        item['comment'] = comment
        print(item)
        df = pd.DataFrame([item], columns=['comment', 'Positive','Neutral', 'Negative', 'Sentiment'])
        df.to_csv(savePath, index=False, mode='a', header=None)
        time.sleep(0.1)

    except TencentCloudSDKException as err:
        print(err)

def read_data(ReadPath, savePath):
    df = pd.read_csv(ReadPath, sep='\t')
    for comment in df.content:
        make_request(comment, savePath)
if __name__ == '__main__':
    # read_data('./data/pre-data/导演创作(13948).csv', './data/finish/导演创作.csv')
    # read_data('./data/pre-data/后期制作(23766).csv', './data/finish/后期制作.csv')
    # read_data('./data/pre-data/拍摄阶段(33341).csv', './data/finish/拍摄阶段.csv')
    read_data('./data/pre-data/演员表现(9122).csv', './data/finish/演员表现.csv')
    # read_data('./data/pre-data/影片题材(38377).csv', './data/finish/影片题材.csv')