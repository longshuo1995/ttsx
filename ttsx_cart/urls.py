
from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('ttsx_user.urls')),
    url(r'^goods/', include('ttsx_goods.urls')),
    url(r'^cart/', include('ttsx_cart.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
]
