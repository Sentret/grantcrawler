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

        grants = response.selector.xpath('//*[@id="block-views-fondcontests-block-1"]/div/div[1]/table/tbody/tr')
 
        for grant in grants:
            item = GrantItem()           
            item['title'] = grant.xpath('td/p/text()').extract()           
            item['date'] = grant.xpath('td[2]/text()').extract()
            item['link'] = "http://www.rscf.ru/ru/contests" 
            print(item['date'])
            yield item
     

