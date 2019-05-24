# -*- coding: utf-8 -*-
import scrapy


class PlGirlSpider(scrapy.Spider):
    name = 'pl_girl'
    allowed_domains = ['pretty.presslogic.com/']
    start_urls = ['https://pretty.presslogic.com/article/302553/%E6%8A%BD%E5%BB%BF%E5%B9%BE%E8%90%AC%E6%B4%97%E9%A0%AD%E6%B0%B4%E8%BF%94%E5%B1%8B%E4%BC%81-%E5%8F%8B%E6%9E%B1vip-%E7%BE%85%E5%AE%B6%E8%8B%B1-%E6%93%BA%E6%98%8E%E8%A3%9D%E6%88%91-%E7%95%B6%E6%99%82%E6%88%91%E5%B7%B2%E7%B6%93%E4%BF%82%E5%85%89%E9%A0%AD-%E7%B6%B2%E6%B0%91-%E5%A5%BD%E9%81%8E2%E8%90%AC%E4%BB%B6%E8%8A%B1%E4%B9%8B%E6%88%80%E5%95%A6']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'render.html',
                    'args': {'wait': 0.5}
                }
            })

    def parse(self, response):
        for option in response.css("p"):
            print(option.xpath("text()").extract())