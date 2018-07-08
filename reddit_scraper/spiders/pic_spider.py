# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule


class PicSpiderSpider(CrawlSpider):
    name = 'pic_spider'
    allowed_domains = ['reddit.com']
    start_urls = ['http://reddit.com/r/pics']

    def parse(self, response):
        pass
