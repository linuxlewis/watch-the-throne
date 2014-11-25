# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20141125_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bathroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('picture', models.FilePathField(path='/Users/Tyler/Github/watch-the-throne/throne/static/bathroom_pics')),
                ('device', models.ForeignKey(to='events.Device')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
