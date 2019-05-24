# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Hk01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    catagories = scrapy.Field()
    publish_date = scrapy.Field()
    update_date = scrapy.Field()
    article = scrapy.Field()
    links = scrapy.Field()
    tags = scrapy.Field()
    refer_link = scrapy.Field()

