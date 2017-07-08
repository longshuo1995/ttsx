# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttsx_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gkucun',
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gsubtitle',
            field=models.CharField(max_length=200),
        ),
    ]
