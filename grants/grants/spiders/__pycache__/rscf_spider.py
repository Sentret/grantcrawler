from __future__ import absolute_import
from scrapy.spider import BaseSpider
from grants.items import GrantItem


class RscfSpider(BaseSpider):
    name = 'rscf'

    allowed_domains = ["http://www.rscf.ru/ru/contests"]
    start_urls = [
        "http://www.rscf.ru/ru/contests"

    ]

    def parse(self, response):

        grants = response.selector.xpath('//body/div/div/div/main/table/tr')
        for grant in grants:
            item = GrantItem()
            item['title'] = grant.xpath('td/a/text()').extract()
            #print(item['title'])    
            item['date'] = grant.xpath('td[5]/text()').extract()
            #print(item['date'])
            yield item
     

