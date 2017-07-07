from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname=models.CharField(default='', max_length=20)
    upwd=models.CharField(default='', max_length=40)
    umail=models.CharField(default='', max_length=30)
    ushou=models.CharField(default='', max_length=20)
    uaddress=models.CharField(default='', max_length=100)
    ucode=models.CharField(default='', max_length=6)
    uphone=models.CharField(default='', max_length=11)
