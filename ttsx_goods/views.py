from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator


def index(request):
    context = {}
    context['top'] = '1'
    type_list = TypeInfo.objects.all()
    list1 = []
    for type in type_list:
        new_list = type.goodsinfo_set.order_by('-id')[0:4]
        click_list = type.goodsinfo_set.order_by('-gclick')[0:4]
        list1.append({'new_list': new_list, 'click_list': click_list, 't1': type})
    context['list1'] = list1
    return render(request, 'ttsx_goods/index.html', {'context': context})

def goods_list(request, tid, index):
    params = request.GET
    order = params.get('order', '--id')
    if order != '--id':
        last_order = request.session.get('order', 'id')
        if order == last_order:
            if order.startswith('-'):
                order = order[1:]
            else:
                order = '-'+order
        print(order)
        request.session['order'] = order
    else:
        order = '-id'
    t1 = TypeInfo.objects.get(pk=tid)
    glist = t1.goodsinfo_set.order_by(order)
    new_list = glist[0:2]

    # 获取分页数据
    page = Paginator(glist, 10).page(index)

    context = {'top': '1', 'cart_show': '1', 't1': t1, 'new_list': new_list, 'page': page}

    return render(request, 'ttsx_goods/list.html', {'context': context})


def goods_detail(request, gid):
    try:
        goods = GoodsInfo.objects.get(pk=gid)
        t1 = goods.gtype
        new_list = t1.goodsinfo_set.order_by('-id')[0:2]
    except:
        return render(request, '404.html')
    context = {'top': '1', 'cart_show': '1', 't1': t1, 'new_list': new_list, 'goods': goods}
    return render(request, 'ttsx_goods/detail.html', {'context': context})
