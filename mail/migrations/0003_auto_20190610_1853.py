# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-10 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_auto_20190610_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='First_Name',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='Last_Name',
            field=models.TextField(max_length=50),
        ),
    ]
