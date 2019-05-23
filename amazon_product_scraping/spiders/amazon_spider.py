# -*- coding: utf-8 -*-
import scrapy


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.com/b/ref=gbpp_itr_m-3_01bf_Arts&Pho?node=1&ie=UTF8']

    def parse(self, response):
        pass
