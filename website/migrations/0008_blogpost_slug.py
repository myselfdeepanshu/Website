# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20160330_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(default=None, max_length=255, null=True),
        ),
    ]
