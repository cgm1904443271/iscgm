# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-07 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0002_mainshow'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodFypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeid', models.CharField(max_length=20)),
                ('typename', models.CharField(max_length=255)),
                ('childtypenames', models.CharField(max_length=200)),
                ('typesort', models.IntegerField()),
            ],
            options={
                'db_table': 'axf_foodtypes',
            },
        ),
    ]
