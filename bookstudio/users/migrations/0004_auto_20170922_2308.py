# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-22 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170917_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
