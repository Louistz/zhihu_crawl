# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request, FormRequest
from zhihu_crawl.settings import HEADER
from zhihu_crawl.tool import http_img
from zhihu_crawl.items import UserItem
from zhihu_crawl.settings import ZHIHU_ACCOUNT
import time

ZHIHU_DOMAIN = u"http://www.zhihu.com"


class ZhihuUserSpider(scrapy.Spider):
    name = "zhihu_user"
    allowed_domains = ["www.zhihu.com"]
    start_urls = [
        "http://www.zhihu.com/people/kaifulee"
    ]

    def parse(self, response):
        url = response.url
        urls = list(url)
        username = url.split("/")[-1:][0]
        user_req_list = []
        user_req_list.append(self.parse_item(response))
        # if username != "zhouzhao":
        #     user_req_list = map(lambda url: Request(response.url,
        #                                             meta={'cookiejar': response.meta['cookiejar']},
        #                                             headers=HEADER,
        #                                             callback=self.parse_item), urls)
        # return Request(u"http://www.zhihu.com/people/zhouzhao/followers",
        #                meta={'cookiejar': response.meta['cookiejar']},
        #                headers=HEADER,
        #                callback=self.parse_item)
        followees_num = self.get_num_from_list(
                response.xpath(
                        '//div[@class="zm-profile-side-following zg-clear"]//a[@class="item"]/strong/text()').extract(),
                index=0)
        followers_num = self.get_num_from_list(
                response.xpath(
                        '//div[@class="zm-profile-side-following zg-clear"]//a[@class="item"]/strong/text()').extract(),
                index=1)

        followes_urls = []
        if followers_num > 0 and username:
            followes_urls.append(ZHIHU_DOMAIN + u"/people/" + username + u"/followers")
        if followees_num > 0 and username:
            followes_urls.append(ZHIHU_DOMAIN + u"/people/" + username + u"/followees")
        print followes_urls
        if len(followes_urls) > 0:
            followes_req_list = map(lambda url: Request(url,
                                                        meta={'cookiejar': response.meta['cookiejar']},
                                                        headers=HEADER,
                                                        callback=self.parse_follows), followes_urls)
            return followes_req_list + user_req_list
        return user_req_list

    def parse_follows(self, response):
        follows_url = response.xpath(
                '//div[@id="zh-profile-follows-list"]//div[@class="zm-list-content-medium"]//h2[@class="zm-list-content-title"]//a/@href').extract()
        follows_req_list = map(lambda url: Request(url,
                                                   meta={'cookiejar': response.meta['cookiejar']},
                                                   headers=HEADER,
                                                   callback=self.parse), follows_url)
        return follows_req_list

    def parse_item(self, response):
        url = response.url
        item = UserItem();
        item['username'] = url.split("/")[-1:][0]
        item['nickname'] = self.get_str_from_list(
                response.xpath(
                    '//div[@class="top"]//div[@class="title-section ellipsis"]//span[@class="name"]/text()').extract())
        item['oneword'] = self.get_str_from_list(
                response.xpath('//div[@class="title-section ellipsis"]/span[@class="bio"]/text()').extract())
        item['location'] = self.get_str_from_list(
                response.xpath('//div[@data-name="location"]//span[@class="location item"]/a/text()').extract())
        item['business'] = self.get_str_from_list(
                response.xpath('//div[@data-name="location"]//span[@class="business item"]/a/text()').extract())
        item['employment'] = self.get_str_from_list(
                response.xpath('//div[@data-name="employment"]//span[@class="employment item"]/a/text()').extract())
        item['position'] = self.get_str_from_list(
                response.xpath('//div[@data-name="employment"]//span[@class="position item"]/a/text()').extract())
        item['education'] = self.get_str_from_list(
                response.xpath('//div[@data-name="education"]//span[@class="education item"]/a/text()').extract())
        item['major'] = self.get_str_from_list(
                response.xpath('//div[@data-name="education"]//span[@class="education-extra item"]/a/text()').extract())
        item['description'] = self.get_str_from_list(
                response.xpath('//div[@data-name="description"]//textarea[@name="description"]/text()').extract())
        item['agrees_num'] = self.get_num_from_list(response.xpath(
                '//div[@class="zm-profile-header-info-list"]//span[@class="zm-profile-header-user-agree"]/strong/text()')
                                                    .extract())
        item['thanks_num'] = self.get_num_from_list(response.xpath(
                '//div[@class="zm-profile-header-info-list"]//span[@class="zm-profile-header-user-thanks"]/strong/text()')
                                                    .extract())
        item['asks_num'] = self.get_num_from_list(
                response.xpath('//div[@class="profile-navbar clearfix"]//a/span[@class="num"]/text()').extract(),
                index=0)
        item['answers_num'] = self.get_num_from_list(
                response.xpath('//div[@class="profile-navbar clearfix"]//a/span[@class="num"]/text()').extract(),
                index=1)
        item['posts_num'] = self.get_num_from_list(
                response.xpath('//div[@class="profile-navbar clearfix"]//a/span[@class="num"]/text()').extract(),
                index=2)
        item['collections_num'] = self.get_num_from_list(
                response.xpath('//div[@class="profile-navbar clearfix"]//a/span[@class="num"]/text()').extract(),
                index=3)
        item['logs_num'] = self.get_num_from_list(
                response.xpath('//div[@class="profile-navbar clearfix"]//a/span[@class="num"]/text()').extract(),
                index=4)

        item['followees_num'] = self.get_num_from_list(
                response.xpath(
                    '//div[@class="zm-profile-side-following zg-clear"]//a[@class="item"]/strong/text()').extract(),
                index=0)
        item['followers_num'] = self.get_num_from_list(
                response.xpath(
                    '//div[@class="zm-profile-side-following zg-clear"]//a[@class="item"]/strong/text()').extract(),
                index=1)
        item['images'] = response.xpath('//div[@class="body clearfix"]//img[@class="Avatar Avatar--l"]/@src').extract()
        item['gender'] = self.get_gender(response.xpath(
                '//div[@class="zm-profile-header-op-btns clearfix"]//button[@data-follow="m:button"]/text()').extract())

        return item

    def get_str_from_list(self, l, index=0, default=""):
        if len(l) > index:
            return l[index]
        else:
            return default

    def get_num_from_list(self, l, index=0, default=0):
        if self.get_str_from_list(l):
            return int(self.get_str_from_list(l, index=index, default=default))
        else:
            return default

    def get_gender(self, l, default=[0, 1, 2]):
        if len(l) == 0:
            return default[0]
        elif l[0] == u"关注他":
            return default[1]
        elif l[0] == u"关注她":
            return default[2]
        else:
            return default[0]

    def start_requests(self):
        print "zhi_hu_spider/////// start_requests"
        return [
            Request("http://www.zhihu.com/#signin",
                    meta={"cookiejar": 1},
                    headers=HEADER,
                    callback=self.post_login)]

    def post_login(self, response):
        print "Preparing login"
        xsrf = response.xpath('//input[@name="_xsrf"]/@value').extract()[0]
        print xsrf
        formdata = {'_xsrf': xsrf,
                    'email': ZHIHU_ACCOUNT['username'],
                    'password': ZHIHU_ACCOUNT['password'],
                    'remember_me': 'true'}
        captcha_xpath = response.xpath('//input[@id="captcha"]')
        if len(captcha_xpath) > 0:
            img_url = "http://www.zhihu.com/captcha.gif?r=" + str(time.time()).split(".")[0]
            http_img.save_url_img(img_url, "captcha.gif")
            captcha = input("please input the captcha:")
            formdata['captcha'] = captcha
        return [FormRequest(url="http://www.zhihu.com/login/email",
                            meta={'cookiejar': 1},
                            method="POST",
                            formdata=formdata,
                            headers=HEADER,
                            callback=self.after_login)]

    def after_login(self, response):
        for url in self.start_urls:
            yield Request(url=url,
                          meta={'cookiejar': response.meta['cookiejar']},
                          headers=HEADER,
                          dont_filter=True)
