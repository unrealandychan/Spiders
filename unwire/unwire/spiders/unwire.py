# -*- coding: utf-8 -*-
import scrapy


class UnwireSpider(scrapy.Spider):
    name = 'unwire'
    start_urls = ['http://unwire.hk/articles/89']

    def parse(self, response):
        for links in response.xpath('//h3/a/@href').extract():
            yield scrapy.Request(url = links,callback = self.sub_parse)

        nextPageUrl = response.xpath('//a[@class="next page-numbers"]/@href')[0].extract()
        if nextPageUrl:
            yield scrapy.Request(url = nextPageUrl,callback=self.parse)



    def sub_parse(self,response):
        item ={
            'url':response.url,
            'date':response.xpath('//meta[@property="og:updated_time"]/@content')[0].extract(),
            'title':response.xpath('//h1//text()')[0].extract(),
            'article':response.xpath('//div[@class= "entry"]//p//text()').extract(),
            'author':response.xpath('//h3[@class="additional"]/a/text()').extract()[0],
            'link':response.xpath('//h1/a/@href').extract()[1],
            'tag':response.xpath('//a[@rel="tag"]/text()').extract()
        }
        yield item

