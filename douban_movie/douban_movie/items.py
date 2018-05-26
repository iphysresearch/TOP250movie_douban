# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# movie_item
class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_id = scrapy.Field()           # 电影的唯一ID
    movie_title = scrapy.Field()        # 电影名字
    release_date = scrapy.Field()       # 电影发布日期
    directedBy = scrapy.Field()         # 电影导演
    starring = scrapy.Field()           # 电影主演
    genre = scrapy.Field()              # 电影类型
    runtime = scrapy.Field()            # 电影时长
    country = scrapy.Field()            # 电影的国别
    language = scrapy.Field()           # 电影的语言
    rating_num = scrapy.Field()         # 电影总评分
    vote_num = scrapy.Field()           # 电影评分人数
    rating_per_stars5 = scrapy.Field()  # 电影5分百分比
    rating_per_stars4 = scrapy.Field()  # 电影4分百分比
    rating_per_stars3 = scrapy.Field()  # 电影3分百分比
    rating_per_stars2 = scrapy.Field()  # 电影2分百分比
    rating_per_stars1 = scrapy.Field()  # 电影1分百分比
    intro = scrapy.Field()              # 电影剧情简介
    comment_num = scrapy.Field()        # 电影短评数
    question_num = scrapy.Field()       # 电影提问数

# movie_comment
class DoubanMovieCommentItem(scrapy.Item):
    useful_num = scrapy.Field()      # 多少人评论有用
    comment_id = scrapy.Field()      # 短评的唯一id
    people = scrapy.Field()          # 评论者名字（唯一）
    people_url = scrapy.Field()      # 评论者页面
    star = scrapy.Field()            # 评分
    content = scrapy.Field()         # 评论内容
    time = scrapy.Field()            # 评论时间
    movie_id = scrapy.Field()        # 电影的唯一ID
    URL = scrapy.Field()             # 该短评所在页面URL
    #comment_page_url = scrapy.Field()# 当前页



# movie_people
class DoubanMovieUser(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    people = scrapy.Field()
    location = scrapy.Field()        # 常居地
    introduction = scrapy.Field()    # 个人简介
    friend = scrapy.Field()          # 好友数（关注的成员数）
    be_attention = scrapy.Field()    # 被关注的成员数

    pass    