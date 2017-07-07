from django.contrib import admin
from .models import *


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle', 'gprice']

admin.site.register(TypeInfo, TypeAdmin)
