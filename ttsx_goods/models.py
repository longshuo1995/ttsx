from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle

class GoodsInofo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='goods/')
    gprice = models.DecimalField(max_digits=5, decimal_places=2)
    gunit = models.CharField(max_length=10)
    gclick = models.IntegerField(default=0)
    gsubtitle = models.CharField(max_length=50)
    # 这个使用富文本编辑器
    gcontent = HTMLField()
    gkucun = models.IntegerField(default=100)
    gtype = models.ForeignKey('TypeInfo')
