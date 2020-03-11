# -*- coding: utf-8 -*-
"""scrapy demo"""
import scrapy


class DemoSpider(scrapy.Spider):
    """demospider jicheng zi spider"""
    name = 'demo'
    # allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/ws/demo.html']

    def parse(self, response):
        filename = response.url.split('/')[-1]
        with open(filename, 'wb') as file:
            file.write(response.body)
