# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import signals
import json
import codecs
from twisted.enterprise import adbapi
from datetime import datetime
from hashlib import md5

class MovieItemPipeline(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_item.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()        

################ People ####################


        
class MovieXPeoplePipeline1040(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_Xpeople1040.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()      

class MoviePeoplePipeline5000(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_people5000.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()      

class MoviePeoplePipeline10000(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_people10000.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close() 

class MoviePeoplePipeline15000(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_people15000.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close() 

class MoviePeoplePipeline20000(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_people20000.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close() 

class MoviePeoplePipeline25000(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_people25000.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close() 

class MoviePeoplePipeline30000(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_people30000.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close() 

class MoviePeoplePipeline35000(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_people35000.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close() 

class MoviePeoplePipeline40000(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_people40000.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()                                                       


################ Comment ####################

class MovieCommentPipeline20(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_comment20.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MovieCommentPipeline40(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_comment40.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MovieCommentPipeline60(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_comment60.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MovieCommentPipeline80(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_comment80.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MovieCommentPipeline100(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_comment100.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MovieCommentPipeline120(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_comment120.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MovieCommentPipeline140(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_comment140.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MovieCommentPipeline160(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_comment160.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MovieCommentPipeline180(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_comment180.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MovieCommentPipeline200(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_comment200.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

class MovieCommentPipeline225(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_comment225.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()


class MovieCommentPipeline250(object):
    def __init__(self):
        self.file = codecs.open('../data/movie_comment250.json', 'w', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()

