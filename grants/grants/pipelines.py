from scrapy import log
from scrapy.exceptions import DropItem
from django.db.utils import IntegrityError
from datetime import datetime
from datetime import date
import re

class GrantPipeline(object):
    def process_item(self, item, spider):

        item['title'] = item['title'][0]
        item['date'] = item['date'][0]    

#поиск даты в строке
        match = re.search(r'\d{2}.\d{2}.\d{4}', item['date'])
        dt = datetime.strptime(match.group(),'%d.%m.%Y').date()
#сравнение даты с текущей, чтобы не добавлять в бд просроченные конкурсы
     
        if date.today() > dt:
     	    return item
     
        item['date'] = dt.strftime('%d.%m.%Y').replace("/",".")    	
        item.save()
	
 	 
        return item


class TpPipeline(object):

    def process_item(self, item, spider):  
        item['link'] = "https://theoryandpractice.ru" + item['link']	
        item.save()	 
        return item