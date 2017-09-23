from __future__ import absolute_import
from scrapy.spiders import Spider
import os

from grants.items import GrantItem



class RfbrSpider(Spider):
    name = 'rfbr'
    allowed_domains = ["http://www.rfbr.ru/rffi/ru/contest"]
    start_urls = [
        "http://www.rfbr.ru/rffi/ru/contest"

    ]

    def parse(self, response):

        grants = response.selector.xpath('//body/div/div/div/main/table/tr')
        
        for grant in grants:
            item = GrantItem()
            item['title'] = grant.xpath('td/a/text()').extract()         
            item['date'] = grant.xpath('td[5]/text()').extract()
            item['link'] ="http://www.rfbr.ru"+ grant.xpath('td/a/@href').extract()[0]           
            yield item
     
