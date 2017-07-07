from django.shortcuts import render
from .models import *


def index(request):
    context = {}
    type_list = TypeInfo.objects.all()
    list1 = []
    for type in type_list:
        new_list = type.goodsinfo_set.order_by('-id')[0:4]
        click_list = type.goodsinfo_set.order_by('-gclick')[0:4]
        list1.append({'new_list': new_list, 'click_list': click_list})
    return render(request, 'ttsx_goods/index.html', {'context': context})
