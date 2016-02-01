# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class UserItem(scrapy.Item):
    username = scrapy.Field()       #用户名
    nickname = scrapy.Field()       #昵称
    oneword = scrapy.Field()        #一句话
    description = scrapy.Field()    #简介
    location = scrapy.Field()       #居住地
    business = scrapy.Field()       #商业
    employment = scrapy.Field()     #行业
    position = scrapy.Field()       #职位
    education = scrapy.Field()      #学习
    major = scrapy.Field()          #专业
    tags = scrapy.Field()           #标签
    agrees_num = scrapy.Field()     #赞同数
    thanks_num = scrapy.Field()     #感谢数
    asks_num = scrapy.Field()       #提问
    answers_num = scrapy.Field()    #回答
    posts_num = scrapy.Field()      #专栏数
    collections_num = scrapy.Field()#收藏数
    logs_num = scrapy.Field()       #编辑数
    followees_num = scrapy.Field()  #关注数
    followers_num = scrapy.Field()  #粉丝数
    images = scrapy.Field()         #图片
    gender = scrapy.Field()         #性别0:default,1:男,2:女
