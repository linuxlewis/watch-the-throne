# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20141001_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('device_guid', models.CharField(max_length=36)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='environmentevent',
            name='device_id',
        ),
        migrations.AddField(
            model_name='environmentevent',
            name='device',
            field=models.ForeignKey(to='events.Device', db_column='other_device_id'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='environmentevent',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='environmentevent',
            name='event_type',
            field=models.CharField(choices=[('lights-on', 'lights-on'), ('lights-off', 'lights-off'), ('sound-on', 'sound-on'), ('sound-off', 'sound-off')], max_length=200),
            preserve_default=True,
        ),
    ]
