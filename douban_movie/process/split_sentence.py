import re
import pandas as pd


def cut_sent(para):
    para = re.sub('([，。！？\?])([^”’])', r"\1\n\2", para)
    para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)
    para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)
    para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
    para = para.rstrip()
    return para.split("\n")


path = '../data/comment.csv'
file = './data/comment.csv'
df = pd.read_csv(path)
contents = df.content.apply(lambda x: str(x))
scentences = [
    scentence for content in contents for scentence in cut_sent(content)]
dataframe = pd.DataFrame({"content": scentences})
dataframe.to_csv(file, index=False, sep='\t', mode='w')
