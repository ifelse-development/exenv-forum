# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=1000)),
                ('answer_rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('tag', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'Date published')),
            ],
        ),
    ]