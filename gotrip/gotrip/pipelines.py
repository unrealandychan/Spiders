# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from scrapy import log
from scrapy.conf import settings

class GotripPipeline(object):
    def process_item(self, item, spider):
        return item



class MongodbPipeline(object):
    def __init__(self):

        client = pymongo.MongoClient(
            host= settings["MONGODB_SERVER"],
            port=settings["MONGODB_PORT"])

        db = client[settings["MONGODB_DB"]]
        self.client = db[settings["MONGODB_COLLECTION"]]


    def process_item(self,item,spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.client.insert(dict(item))
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item
