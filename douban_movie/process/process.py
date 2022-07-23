from textwrap import indent
from matplotlib.pyplot import flag
from numpy import array
import pandas as pd
actor_performance = ['演员']

director_creation = ['导演']

film_theme = ['创世', '温情', '有效性', '女性', '现实', '特色', '大胆', '思路',
              '大片', '女性', '历史', '暴力', '人性', '影片', '社会', '情感', '时代']

shooting_stage = ['画面', '切换', '场景', '镜头', '情节', '灯光', '时间', '演员', '主线']

post_production = ['特效', '剪辑', '配音', '字幕', '摄影', '配乐', '特写', '布景', '转场', '节奏感']

df = pd.read_csv('./data/comment.csv', sep='\t')


def save_comment(arr, title):
    array = []
    for item in arr:
        flag = df['content'].apply(lambda x: str(x)).str.contains(item)
        actor_performance_arr = df[flag].content
        for item in actor_performance_arr:
            array.append(item)
    dataframe = pd.DataFrame({"content": array})
    filePath = './data/{title}({len}).csv'.format(title=title, len=len(array))
    dataframe.to_csv(filePath, index=False, sep='\t', mode='w')


# 获取演员表现相关评论
save_comment(actor_performance, '演员表现')
save_comment(director_creation, '导演创作')
save_comment(film_theme, '影片题材')
save_comment(shooting_stage, '拍摄阶段')
save_comment(post_production, '后期制作')
