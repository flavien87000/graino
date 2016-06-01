# URLconf
from django.conf.urls import include, url
from django.contrib import admin

from graino.views import *
from variety.views import *
from category.views import *

urlpatterns = [
    url(r'^varieties/', variety_list_view, name='variety_list_view'),
    url(r'^categories/(?P<category>[\w-]+)/$', category_detail, name='category_detail'),
]