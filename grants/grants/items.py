import scrapy
from scrapy_djangoitem import DjangoItem
from app.models import Grant


class GrantItem(DjangoItem):

    django_model = Grant
    
