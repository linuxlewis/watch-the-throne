# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnvironmentEvent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('event_type', models.CharField(choices=[('lights-on', 'lights-on'), ('lights-off', 'lights-off')], max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
