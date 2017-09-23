from __future__ import absolute_import
from scrapy.spider import BaseSpider
from grants.items import GrantItem


class TPSpider(BaseSpider):
    custom_settings = {
        'ITEM_PIPELINES': {
            'grants.pipelines.TpPipeline': 1000
        }
    }
    name = 'theory_and_practise'

    allowed_domains = ["https://theoryandpractice.ru/grants?disciplines=informatsionnye-tekhnologii&purposes=research"]
    start_urls = [
        "https://theoryandpractice.ru/grants?disciplines=informatsionnye-tekhnologii&purposes=research"

    ]

    def parse(self, response):


        grants = response.selector.xpath('//div[@class="preview-box-platform"]')
        print (grants)
        for grant in grants:
            item = GrantItem() 
            item['title'] = grant.xpath('a/div/div[@class="preview-box-platform-title"]/text()').extract()[0]               
            item['date'] = grant.xpath('a/div/div[@class="preview-box-platform-uptitle font-size-uptitle-small"]/text()').extract()[0]           
            item['link'] = grant.xpath('a/@href').extract()[0]
            yield item
     