# -*- coding: utf-8 -*-
import scrapy


class GotripAllSpider(scrapy.Spider):
    name = 'gotrip_all'
    allowed_domains = ['gotrip.hk']
    start_urls = [
        "https://www.gotrip.hk/category/itineraryguide/japan_guide/",
        "https://www.gotrip.hk/category/itineraryguide/korea_guide/",
        "https://www.gotrip.hk/category/itineraryguide/taiwan_guide/",
        "https://www.gotrip.hk/category/itineraryguide/macau_guide/",
        "https://www.gotrip.hk/category/travel_hacker/",
        "https://www.gotrip.hk/category/weekend_lifestyle/",
        "https://www.gotrip.hk/category/ladies_talk/",
        "https://www.gotrip.hk/category/excitement/",
        'https://www.gotrip.hk/columns/']

    def parse(self, response):
        for link in response.xpath('//div[@class="article--grid__header"]/a/@href').extract():
            yield scrapy.Request(url = link,callback = self.sub_parse)

        nextLink = response.xpath('//a[@class="next page-numbers"]/@href').extract()[0]

        if nextLink:
            yield scrapy.Request(url=nextLink,callback=self.parse)

    def sub_parse(self,response):
        items = {
            "url":response.url,
            "title": response.xpath('//h1[@class="article__title  article__title--single"]//text()')[0].extract(),
            "catagory": response.xpath('//div[@class="article__author-name"]//text()')[0].extract(),
            "publish_time": response.xpath('//time/@datetime')[0].extract(),
            'article': response.xpath("//div[contains(@class,'_page_')]//text()").extract(),
            'tags': response.xpath("//a[@class='btn  btn--small  btn--tertiary']//text()")[6:-6].extract()

        }

        yield items