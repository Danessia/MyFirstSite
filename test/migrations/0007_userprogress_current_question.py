# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 12:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0006_auto_20180119_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprogress',
            name='current_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test.Question'),
        ),
    ]