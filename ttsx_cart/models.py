from django.db import models
from ttsx_user import UserInfo


class CartInfo(models.Model):
    goods = models.ForeignKey('ttsx_goods.GoodsInfo')
    user = models.ForeignKey(UserInfo)
