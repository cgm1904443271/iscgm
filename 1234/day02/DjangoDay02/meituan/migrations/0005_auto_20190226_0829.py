# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-02-26 08:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meituan', '0004_auto_20190226_0827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['s_score']},
        ),
    ]
