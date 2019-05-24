# -*- coding: utf-8 -*-
import scrapy
import re


class Hk01allSpider(scrapy.Spider):
    name = 'hk01all'
    allowed_domains = ['hk01.com']
    start_urls = ['https://www.hk01.com/數碼生活/331297/']

    def parse(self, response):
        item = {
            'url':response.url,
            'title':response.xpath('//h1//text()')[0].extract(),
            'author':response.xpath('//div[@class="sc-bdVaJa jJqEVj"]/a/text()').extract(),
            'catagory':response.xpath('//article//text()')[0].extract(),
            'publish_date':response.xpath('//time/text()')[0].extract(),
            'update)date':response.xpath('//time/text()')[1].extract(),
            'article':response.xpath('//article//text()').extract()[6:],
            'tags':response.xpath("//span//span/text()").extract(),
            'refer_link':response.xpath("//div[@class='sc-bwzfXH fkKzgp']//a/@href").extract()


        }
        yield item

        links = response.xpath('//a/@href').extract()

        for link in links:
            if re.match(r'^/[數碼生活|遊戲動漫|GEME]',link):
                yield scrapy.Request(url = "https://hk01.com"+link,callback=self.parse)
