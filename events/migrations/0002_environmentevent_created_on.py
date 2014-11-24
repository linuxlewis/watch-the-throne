# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='environmentevent',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2014, 10, 1, 3, 53, 55, 52457)),
            preserve_default=True,
        ),
    ]
