# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-20 06:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_shop_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='photo',
        ),
    ]
