# coding : utf-8

from datetime import datetime

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from crawl.items import NewItem

class KnctSpider(BaseSpider):
    name = 'knct'
    allowed_domains = ['http://www.kumamoto-nct.ac.jp/']
    start_urls =[
         'http://www.kumamoto-nct.ac.jp/announce/'
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        sites = hxs.select('//ul/li')
        items =[]

        for site in sites:
            item = NewItem()
            item['title'] = site.select('a/text()').extract()
            items.append(item)
        for item in items:
            yield item
