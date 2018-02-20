# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0002_auto_20180116_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complexity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('level', models.PositiveIntegerField(default=1)),
                ('series', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='complexity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test.Complexity'),
        ),
    ]