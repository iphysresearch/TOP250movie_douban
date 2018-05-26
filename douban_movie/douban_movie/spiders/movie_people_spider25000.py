# -*- coding: utf-8 -*-

import scrapy
import numpy as np
from faker import Factory
from douban_movie.dns_cache import _setDNSCache
from douban_movie.items import DoubanMovieItem, DoubanMovieCommentItem, DoubanMovieUser
# import urlparse  # python2.x
from urllib import parse as urlparse  # python3.x
f = Factory.create()


class DoubanPeopleSpider(scrapy.Spider):
           
    name = 'douban-people25000'
    allowed_domains = ['accounts.douban.com', 'douban.com','movie.douban.com']
    start_urls = [
        'https://movie.douban.com/'
    ]
    custom_settings = { # 自定义该spider的pipeline输出
        'ITEM_PIPELINES': {
            'douban_movie.pipelines.MoviePeoplePipeline25000': 1,
        },
        'DOWNLOAD_DELAY': 1.8, 
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
        #print(response.status)
        print('after_login!')
        #_setDNSCache()
        #print()
        self.headers['Host'] = "www.douban.com" 
        
        people_url = np.loadtxt('people_url.out', dtype='|S').tolist()[20000:25000]    # 38599
        for url in people_url:        
            yield scrapy.Request(url=url.decode(), #% people_url,
                            meta={'cookiejar': response.meta['cookiejar']},
                            headers=self.headers,
                            callback=self.parse_people_url)



    # 废弃的parse
    def parse_people_url(self, response):
        #print(response.status)
        _setDNSCache()
        User = DoubanMovieUser()
        User['location'] = response.xpath('//*[@id="profile"]/div/div[2]/div[1]/div/a/text()').extract()
        User['location'] = response.xpath('//div[@class="user-info"]/a/text()').extract()
        User['introduction'] = response.xpath('//span[@id="intro_display"]/text()').extract()
        User['friend'] = response.xpath('//div[@id="friend"]/h2/span/a/text()').extract()
        User['be_attention'] = response.xpath('//p[@class="rev-link"]/a/text()').extract()
        yield User

