# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20141125_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='device_guid',
            field=models.CharField(unique=True, max_length=36),
            preserve_default=True,
        ),
    ]
