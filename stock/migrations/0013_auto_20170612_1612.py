# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 12:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0012_auto_20170612_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockpfdates',
            name='pfDate',
            field=models.DateField(default=datetime.datetime(2017, 6, 12, 12, 12, 33, 176658, tzinfo=utc)),
        ),
    ]
