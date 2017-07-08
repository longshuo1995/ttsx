
from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^goods_list(\d+)_(\d+)/', goods_list),
    url('^goods_detail(\d+)/', goods_detail),
    url(r'^', index),
]
