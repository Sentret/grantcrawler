from django.conf.urls import include, url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^djangoadmin',  admin.site.urls),
    url(r'^$', views.grant_list),
    
]
