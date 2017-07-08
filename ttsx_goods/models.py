from django.db import models
from tinymce.models import HTMLField


class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='goods/')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gclick = models.IntegerField(default=0)
    gunit = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)
    gsubtitle = models.CharField(max_length=200)
    # 这个使用富文本编辑器
    gkucun = models.IntegerField(default=200)
    gcontent = HTMLField()
    gtype = models.ForeignKey('TypeInfo')
