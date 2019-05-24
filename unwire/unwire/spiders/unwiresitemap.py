# -*- coding: utf-8 -*-
import scrapy

class UnwiresitemapSpider(scrapy.spiders.SitemapSpider):
    name = 'unwiresitemap'
    sitemap_urls = ['https://unwire.hk/sitemap.xml']

    def parse(self, response):
        item = {
            'date':response.xpath('//meta[@property="og:updated_time"]/@content')[0].extract(),
            'title':response.xpath('//h1//text()')[0].extract(),
            'article':response.xpath('//div[@class= "entry"]/p/text()').extract(),
            'author':response.xpath('//h3[@class="additional"]/a/text()').extract(),
            'link':response.xpath('//h1/a/@href').extract()[1],
        }
        yield item