# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_questionpost_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionpost',
            name='file',
            field=models.FileField(default='', upload_to=None),
            preserve_default=False,
        ),
    ]
