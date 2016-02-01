# coding=utf-8
from zhihu_crawl.settings import MONGO
from pymongo import MongoClient


class ZhihuUserMongoPipeline(object):
    settings = None
    db = None

    @classmethod
    def from_crawler(cls,crawler):
        ext = cls()
        ext.settings = MONGO
        ext.db = MongoClient(ext.settings['host'],ext.settings['port'])['zhihu']['user']
        return ext

    def process_item(self,item,spider):
        doc = dict(item)
        doc['_id'] = doc['username']
        print doc
        if self.db.count({'_id':doc['_id']}) == 0 :
            self.db.insert_one(doc)
            print "save item"
        return item