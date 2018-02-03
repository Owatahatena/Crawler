# coding : utf-8

from datetime import datetime
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
from aspiring.items import AspiringItem

class AspiringSpider(BaseSpider):
    name = 'aspiring'
    allowed_domains = ['http://www.kumamoto-nct.ac.jp/']
    start_urls =[
         'http://www.kumamoto-nct.ac.jp/entrance/exam/honka-exam/exam-data-past.html'
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)

        sites = hxs.select('//ul/li')
        items =[]

        for site in sites:
            item = AspiringItem()
            item['years'] = site.select('h5/text()').extract()
            items.append(item)
        for item in items:
            yield item
