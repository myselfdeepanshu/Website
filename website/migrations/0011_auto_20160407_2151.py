# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_textdescription_text_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to=b'blog/images/'),
        ),
    ]
