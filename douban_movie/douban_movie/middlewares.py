# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

from selenium import webdriver
from scrapy.http import HtmlResponse
from lxml import etree
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import choice

#     header 
ua_list = [
          "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/48.0.2564.82 Chrome/48.0.2564.82 Safari/537.36",
          "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
          "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
          "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
          "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36"
]

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.resourceTimeout"] = 15 
dcap["phantomjs.page.settings.loadImages"] = False
dcap["phantomjs.page.settings.userAgent"] = choice(ua_list)
#driver = webdriver.PhantomJS(executable_path='/home/icgoo/pywork/spider/phantomjs',desired_capabilities=dcap)
#driver = webdriver.PhantomJS(executable_path=u'/home/fank/pywork/spider/phantomjs',desired_capabilities=dcap)
#driver = webdriver.Firefox()
#driver = webdriver.Chrome()

class SeleniumMiddleware(object):
    #
    def process_request(self, request, spider):

        if spider.name == 'douban-people': #     
            try:
                driver = webdriver.PhantomJS(executable_path= './phantomjs-2.1.1-linux-x86_64/bin/phantomjs') #  PhantomJS
                driver.get(request.url) #         
                driver.implicitly_wait(3) #   3s     
                time.sleep(5) #   5s
                page = driver.page_source
                driver.close()
                #print(page)
                return HtmlResponse(request.url,
                                    body = page,
                                    encoding = 'utf-8',
                                    request = request,)
            except:
                print("get douban-people data failed")


class DoubanMovieSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
