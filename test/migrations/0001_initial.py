# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-16 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('question', models.TextField()),
                ('var1', models.CharField(max_length=200)),
                ('var2', models.CharField(max_length=200)),
                ('var3', models.CharField(max_length=200)),
                ('choice', models.CharField(default='', max_length=200)),
                ('complexity', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
