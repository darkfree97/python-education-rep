# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-29 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20161229_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
