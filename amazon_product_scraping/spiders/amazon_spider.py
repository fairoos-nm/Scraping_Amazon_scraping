# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonProductScrapingItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com/b/ref=gbpp_itr_m-3_01bf_Arts&Pho?node=1&ie=UTF8']

    def parse(self, response):
        items = AmazonProductScrapingItem()

        product_name = response.css('.s-access-title::text').extract()
        product_author = response.css('.a-color-secondary .a-text-normal').css('::text').extract()
        product_price = response.css('.a-spacing-none:nth-child(2) .sx-price-large').css('::text').extract()
        product_link = response.css('.cfMarker::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_link'] = product_link

        yield items
