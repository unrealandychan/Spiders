# -*- coding: utf-8 -*-
import scrapy
import requests
import re


class HypebeastSpider(scrapy.Spider):
    name = 'hypebeast'
    start_urls = ['https://hypebeast.com/zh/page/1']
    page = 2
    def parse(self, response):



        for link in response.xpath("//div[@class='post-box-content-title']/a/@href").extract():
            yield scrapy.Request(url=link, callback=self.sub_parse)

        if  requests.get('http://hypebeast.com/zh/page/{}'.format(HypebeastSpider.page)).status_code == 200:
            HypebeastSpider.page+=1
            yield scrapy.Request(url='http://hypebeast.com/zh/page/{}'.format(HypebeastSpider.page), callback=self.parse)


    def sub_parse(self,response):
        item = {
            'url':response.url,
            'title':response.xpath('//h1/span/text()').extract(),
            'sub_title':response.xpath('//h2[@class="post-body-excerpt"]/text()').extract(),
            'category':response.xpath('//span[@class="post-body-top-bar-category"]/a/text()').extract(),
            'author':response.xpath('//div[contains(@class,"post-body-sidebar-author")]//a/text()').extract(),
            'article':response.xpath('//article//p/text()').extract(),
            'tags':response.xpath("//div[@class='post-body-content-tags']/div/a/text()").extract(),
            'hype_count':re.findall(r'\d+,*\d+',response.xpath('//span[@class="hype-count"]').extract()[0]),
            'article_links':response.xpath('//article//a/@href').extract(),
            'article_links_text': response.xpath('//article//a//text()').extract(),
            'refer_links':response.xpath("//div[@id='post-footer-related-posts']//div[@class='post-box-content-title']/a/@href").extract(),
            'refer_links_text':response.xpath("//div[@id='post-footer-related-posts']//a//text()").extract()
        }
        yield item