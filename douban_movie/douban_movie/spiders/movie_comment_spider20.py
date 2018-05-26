# -*- coding: utf-8 -*-

import scrapy
import numpy as np
from faker import Factory
from douban_movie.dns_cache import _setDNSCache
from douban_movie.items import DoubanMovieItem, DoubanMovieCommentItem, DoubanMovieUser
# import urlparse  # python2.x
from urllib import parse as urlparse  # python3.x
f = Factory.create()


class DoubanCommentSpider(scrapy.Spider):
    def __init__(self, pages = 1000): 
       """初始化起始页面
       """  
       super(DoubanCommentSpider, self).__init__()
       self.pages = int(pages) -1 #参数pages由此传入, 表示点击下一页的次数
       self.page = 0
       self.url_set = [] #话题url的集合  
       #self.start_urls = ['http://buluo.qq.com/p/barindex.html?bid=%s' % bid]  
       #self.allowed_domain = 'buluo.qq.com'  
       #self.driver = webdriver.Firefox()         
       #self.driver.set_page_load_timeout(5) 
       #throw a TimeoutException when thepage load time is more than 5 seconds.  
         
    name = 'douban-comment20'
    allowed_domains = ['accounts.douban.com', 'douban.com','movie.douban.com']
    start_urls = [
        'https://movie.douban.com/'
    ]
    custom_settings = { # 自定义该spider的pipeline输出
        'ITEM_PIPELINES': {
            'douban_movie.pipelines.MovieCommentPipeline20': 1,
        },
        'DOWNLOAD_DELAY': 2.0,
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
        print(response.status)
        print('after_login!')
        _setDNSCache()
        print()
        self.headers['Host'] = "movie.douban.com" 
        movie_id = np.loadtxt('movie_id.out', dtype='i').tolist()[:20]   # Top250
        for mid in movie_id:
            yield scrapy.Request(url='https://movie.douban.com/subject/%s/comments' % mid,
                              meta={'cookiejar': response.meta['cookiejar']},
                              headers=self.headers,
                              callback=self.parse_comment_url)
            yield scrapy.Request(url='https://movie.douban.com/subject/%s/comments' % mid,
                                                      meta={'cookiejar': response.meta['cookiejar']},
                                                      headers=self.headers,
                                                      callback=self.parse_next_page,
                                                      dont_filter = True)

    def parse_next_page(self, response):
        #print(response.status)
        print('Next_page!')
        print()
        _setDNSCache()
        next_url = response.urljoin(response.xpath('//a[@class="next"]/@href').extract()[0])
        self.url_set.append(next_url)

        try: 
            #next_url = response.urljoin(response.xpath('//a[@class="next"]/@href').extract()[0])
            if next_url and ( self.page < self.pages):
                self.page += 1
                ## 将 「下一页」的链接传递给自身，并重新分析
                yield scrapy.Request(url=next_url,
                              meta={'cookiejar': response.meta['cookiejar']},
                              headers=self.headers,
                              callback=self.parse_next_page,
                              dont_filter = True)
            else:
                print('No more pages!')
                #with open('url_set.txt', mode='w') as f:  
                #    f.write(self.url_set)
                print(self.url_set)
                for url in self.url_set:
                    yield scrapy.Request(url=url,
                                          meta={'cookiejar': response.meta['cookiejar']},
                                          headers=self.headers,
                                          callback=self.parse_comment_url#,
                                          #dont_filter = True
                                          )                
                
        except:
            print("Next page Error")
            print(response.status)
            print(response.urljoin(response.xpath('//a[@class="next"]/@href').extract()))
            return



    def parse_comment_url(self, response):
        #print(response.status)
        print('comment_url!')
        _setDNSCache()
        print()
        comment = DoubanMovieCommentItem()
        comment['movie_id'] = response.xpath('//div[@class="fright"]/a/@name').extract()
        comment['URL'] = response.url
        for item in response.xpath('//div[@class="comment-item"]'):
            # 短评的唯一id
            comment['comment_id'] = int(item.xpath('div[@class="comment"]/h3/span[@class="comment-vote"]/input/@value').extract()[0].strip())
            # 多少人评论有用
            comment['useful_num'] = item.xpath('div[@class="comment"]/h3/span[@class="comment-vote"]/span/text()').extract()[0].strip()
            # 评分
            comment['star'] = item.xpath('div[@class="comment"]/h3/span[@class="comment-info"]/span[2]/@class').extract()[0].strip()
            # 评论时间
            comment['time'] = item.xpath('div[@class="comment"]/h3/span[@class="comment-info"]/span[@class="comment-time "]/@title').extract()
            # 评论内容
            comment['content'] = item.xpath('div[@class="comment"]/p/text()').extract()
            # 评论者名字（唯一）
            comment['people'] = item.xpath('div[@class="avatar"]/a/@title').extract()[0]
            # 评论者页面
            comment['people_url'] = item.xpath('div[@class="avatar"]/a/@href').extract()[0]
            

            # 已摒弃
            #url = item.xpath('div[@class="avatar"]/a/@href').extract()[0]
            #movie_url = item.xpath('//p[@class="pl2"]/a/@href').extract()[0]

            yield comment

