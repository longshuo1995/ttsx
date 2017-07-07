
from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^register/$', register),
    url(r'^register_handle/$', register_handle),
    url(r'^login/$', login),
    url(r'^login_handle/$', login_handle),
    url(r'^center/$', center),
    # info 没有改过来，干脆和center用同一个方法来处理就能解决了
    url(r'^info/$', center),
    url(r'^order/$', order),
    url(r'^site/$', site),
    url(r'^invalidate_username/$', register_valide),
    url(r'^logout/$', logout),
]
