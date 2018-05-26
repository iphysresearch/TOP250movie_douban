# -*- coding: utf-8 -*-

import scrapy
import numpy as np
from faker import Factory
from douban_movie.dns_cache import _setDNSCache
from douban_movie.items import DoubanMovieItem, DoubanMovieCommentItem, DoubanMovieUser
try:
    import urlparse  # python2.x
except:
    from urllib import parse as urlparse  # python3.x
f = Factory.create()


class DoubanMovieSpider(scrapy.Spider):
    name = 'douban-movie'
    allowed_domains = ['accounts.douban.com', 'douban.com','movie.douban.com']
    start_urls = [
        'https://movie.douban.com/'
    ]
    custom_settings = { # 自定义该spider的pipeline输出
        'ITEM_PIPELINES': {
            'douban_movie.pipelines.MovieItemPipeline': 1,
        }
    } 

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Host': 'accounts.douban.com',
        'User-Agent': f.user_agent()
    }

    formdata = {
        'form_email': 'wctttty@163.com',
        'form_password': 'WCy3968113',
        # 'captcha-solution': '',
        # 'captcha-id': '',
        'login': '登录',
        'redir': 'https://movie.douban.com/',
        #'redir': 'https://movie.douban.com/subject/1299361/comments?status=P',
        'source': 'None'
    }

    def start_requests(self):
        return [scrapy.Request(url='https://www.douban.com/accounts/login',
                               headers=self.headers,
                               meta={'cookiejar': 1},
                               callback=self.parse_login)]

    def parse_login(self, response):
        # 如果有验证码要人为处理
        print('Loging...')
        link = response.xpath('.//img[@id="captcha_image"]/@src').extract()
        if len(link) > 0:
            print("此时有验证码")
            #if 'captcha_image' in response.body:
            print('Copy the link:')
            #link = response.xpath('//img[@id="captcha_image"]/@src').extract()[0]
            print(link)
            captcha_solution = input('captcha-solution:')
            captcha_id = urlparse.parse_qs(urlparse.urlparse(link[0]).query, True)['id']
            self.formdata['captcha-solution'] = captcha_solution
            self.formdata['captcha-id'] = captcha_id
        return [scrapy.FormRequest.from_response(response,
                                                 formdata=self.formdata,
                                                 headers=self.headers,
                                                 meta={'cookiejar': response.meta['cookiejar']},
                                                 callback=self.after_login
                                                 )]

    def after_login(self, response):
        _setDNSCache()
        #print(response.status)
        self.headers['Host'] = "movie.douban.com"
        movie_id = np.loadtxt('movie_id.out', dtype='i').tolist()   # Top250
        for mid in movie_id:
            yield scrapy.Request(url='https://movie.douban.com/subject/%s/' % mid,
                              meta={'cookiejar': response.meta['cookiejar']},
                              headers=self.headers,
                              callback=self.parse_movie)


    def parse_movie(self, response):
        print(response.status)
        _setDNSCache()
        movie_item = DoubanMovieItem()
        # movie id
        movie_item['movie_id'] = response.xpath('.//li/span[@class="rec"]/@id').extract()
        # movie title
        movie_item['movie_title'] = response.xpath('.//h1/span[@property="v:itemreviewed"]/text()').extract()
        # release_date
        movie_item['release_date'] = response.xpath('.//h1/span[@class="year"]/text()').extract()
        # 导演
        movie_item['directedBy'] = response.xpath('.//a[@rel="v:directedBy"]/text()').extract()
        # 电影主演
        movie_item['starring'] = response.xpath('.//a[@rel="v:starring"]/text()').extract()
        # 电影类别
        movie_item['genre'] = response.xpath('.//span[@property="v:genre"]/text()').extract()
        # 电影时长
        movie_item['runtime'] = response.xpath('.//span[@property="v:runtime"]/text()').extract()
        # 电影的国别和语言
        temp = response.xpath('.//div[@id="info"]/text()').extract()
        movie_item['country'] = [p for p in temp if (p.strip() != '') & (p.strip() != '/')][0].strip()
        movie_item['language'] = [p for p in temp if (p.strip() != '') & (p.strip() != '/')][1].strip()
        # 电影的评分
        movie_item['rating_num'] = response.xpath('.//strong[@class="ll rating_num"]/text()').extract()
        # 评分的人数
        movie_item['vote_num'] = response.xpath('.//span[@property="v:votes"]/text()').extract()
        # 电影1-5星的百分比
        movie_item['rating_per_stars5'] = response.xpath('.//span[@class="rating_per"]/text()').extract()[0].strip()
        movie_item['rating_per_stars4'] = response.xpath('.//span[@class="rating_per"]/text()').extract()[1].strip()
        movie_item['rating_per_stars3'] = response.xpath('.//span[@class="rating_per"]/text()').extract()[2].strip()
        movie_item['rating_per_stars2'] = response.xpath('.//span[@class="rating_per"]/text()').extract()[3].strip()
        movie_item['rating_per_stars1'] = response.xpath('.//span[@class="rating_per"]/text()').extract()[4].strip()
        # 电影的剧情简介
        intro = response.xpath('.//span[@class="all hidden"]/text()').extract()
        if len(intro):
            movie_item['intro'] = intro
        else:
            movie_item['intro'] = response.xpath('.//span[@property="v:summary"]/text()').extract()
        # 电影的短评数
        movie_item['comment_num'] = response.xpath('.//div[@class="mod-hd"]/h2/span/a/text()').extract()[0].strip()
        # 电影的提问数
        movie_item['question_num'] = response.xpath('.//div[@class="mod-hd"]/h2/span/a/text()').extract()[1].strip()

        # 最后输出
        yield movie_item


