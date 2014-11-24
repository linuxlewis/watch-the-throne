# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_environmentevent_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='environmentevent',
            name='device_id',
            field=models.CharField(max_length=36, default='some-value'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='environmentevent',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 1, 3, 55, 58, 182573), auto_now_add=True),
        ),
    ]
