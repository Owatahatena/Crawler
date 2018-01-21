from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from LinkScrapy.items import LinkscrapyItem

class LinkSpider(CrawlSpider):
    name = 'geturl'
    allwed_domains = ['www.kumamoto-nct.ac.jp']
    start_urls = ['http://www.kumamoto-nct.ac.jp']

    rules = [Rule(LinkExtractor(allow_domains = allwed_domains), callback='parse_link', follow=True)]


    def parse_link(self, respose):
        sel = Selector(respose)
        item = LinkscrapyItem()
        item['url'] = respose.url

        item['title'] = sel.xpath('/html/head/title/text()').extract()

        return item
