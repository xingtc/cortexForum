# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 10:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0010_auto_20160311_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumuser',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 11, 10, 26, 36, 975474, tzinfo=utc)),
        ),
    ]