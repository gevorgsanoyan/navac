# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 12:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliomanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmusers',
            name='cDate',
            field=models.DateField(default=datetime.datetime(2017, 6, 12, 12, 19, 57, 412255, tzinfo=utc)),
        ),
    ]
