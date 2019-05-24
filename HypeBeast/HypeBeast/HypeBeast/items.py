# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HypebeastItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    subtitle =scrapy.Field()
    category=scrapy.Field()
    article = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    hype_count=scrapy.Field()
    article_links = scrapy.Field()
    article_links_text=scrapy.Field()
    refer_links = scrapy.Field()
    refer_links_text=scrapy.Field()