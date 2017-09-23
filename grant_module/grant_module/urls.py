from django.conf.urls import include, url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^djangoadmin',  admin.site.urls, name = 'admin_page'),
    url(r'^$', views.grant_list, name='grant_list'),
    url(r'^crawl$', views.crawler)
    
]
