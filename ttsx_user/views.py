from django.shortcuts import render, redirect
from django.http import JsonResponse
from .user_decorators import user_islogin

from .models import UserInfo
from hashlib import sha1
import datetime


def register(request):
    context ={}
    context['top'] = 0
    context['title'] = '用户注册'
    return render(request, 'ttsx_user/register.html', {'cotext': context})


def register_handle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    uemail = post.get('email')
    user = UserInfo()
    context = {}
    context['top'] = 0
    context['title'] = '用户注册'
    # 考虑到用户将js禁用的情况，需要重新验证一遍
    if len(uname) < 5 or len(uname) > 20:
        context['user_error'] = '请您输入5-20位的合法用户名'
        return render(request, 'ttsx_user/register.html', {'context': '请你输入5-20位的用户名'})
    res_count = UserInfo.objects.filter(uname=uname).count()
    if res_count >= 1:
        context['user_error'] = '经过验证，用户名已经存在！请重新输入'
        return render(request, 'ttsx_user/register.html', {'context': context})

    user.uname = uname
    user.upwd = upwd
    user.umail = uemail
    user.save()
    request.session['uid'] = UserInfo.objects.filter(uname=uname)[0].pk
    response = redirect('/user/login/')
    return response


def register_valide(request):
    uname = request.POST.get('uname')
    csrf = request.POST.get('csrfmiddlewaretoken')
    data = UserInfo.objects.filter(uname=uname).count()
    context = {'data': data}
    return JsonResponse(context)


def login(request):
    context = {}
    context['top'] = 0
    context['title'] = '用户登录'
    try:
        a = request.session['uid']
        res = UserInfo.objects.filter(pk=request.session['uid'])
        if len(res) > 0:
            user = res[0]
            context['uname'] = user.uname
            context['upwd'] = user.upwd
    except Exception as e:
        print('木有信息')
    return render(request, 'ttsx_user/login.html', {'context': context})


def login_handle(request):
    context = {}
    context['top'] = 0
    context['title'] = '用户登录'
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    ujz = post.get('ujz', 0)
    result = UserInfo.objects.filter(uname=uname)
    if len(result) == 0:
        context['user_error'] = '用户名不存在'
        url_path = 'ttsx_user/login.html'
        return render(request, url_path, {'context': context})
    else:
        if result[0].upwd == upwd:
            # 登录成功
            url_path = '/user/center'
            try:
                url_path = request.session['url_path']
            except Exception as e:
                print('出现异常，已经处理了~~~')
                pass
            response = redirect(url_path)
            request.session['luid'] = result[0].id
            request.session['uname'] = result[0].uname
            if ujz == 'user_remember':
                request.session['uid'] = result[0].id
            else:
                print('忘了吧~~')
                request.session['uid'] = 1
            return response
        else:
            context['pwd_error'] = '密码错误'
            return render(request, 'ttsx_user/login.html', context)


@user_islogin
def center(request):
    context = {}
    context['top'] = '1'
    print('center 开始处理')
    context['title'] = '天天生鲜-用户中心哈哈哈'
    try:
        user = UserInfo.objects.get(pk=request.session['luid'])
        context['user'] = user
    except Exception as e:
        pass
    return render(request, 'ttsx_user/user_center_info.html', {'context': context})


@user_islogin
def order(request):
    context = {}
    context['top'] = '1'
    return render(request, 'ttsx_user/user_center_order.html', {'context': context})


@user_islogin
def site(request):
    context = {}
    context['top'] = '1'
    try:
        user = UserInfo.objects.get(pk=request.session['luid'])
        if request.method == 'POST':
            post = request.POST
            ushou = post.get('ushou')
            uaddress = post.get('uaddress')
            ucode = post.get('ucode')
            uphone = post.get('uphone')

            user.ushou = ushou
            user.uaddress = uaddress
            user.ucode = ucode
            user.uphone = uphone
            print('准备保存了噢。。。')
            print(user.id)
            user.save()
            print('保存完毕~~')

        else:
            pass
    except Exception as e:
        print(e)
        pass
    context['user'] = user
    return render(request, 'ttsx_user/user_center_site.html', {'context':context})


def logout(request):
    request.session.flush()
    return redirect('/user/login/')
