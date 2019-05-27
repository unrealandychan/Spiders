# -*- coding: utf-8 -*-
import scrapy


class HktvmallSupermarketSpider(scrapy.Spider):
    name = 'hktvmall_supermarket'
    allowed_domains = ['hktvmall.com/hktv/zh/supermarket']
    start_urls = ['http://hktvmall.com/hktv/zh/supermarket/']

    def parse(self, response):
        pass
