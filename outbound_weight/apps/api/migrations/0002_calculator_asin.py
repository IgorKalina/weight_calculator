# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-01-30 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculator',
            name='asin',
            field=models.CharField(max_length=16, null=True),
        ),
    ]