# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('throne', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BathroomAlert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=10)),
                ('bathroom', models.ForeignKey(to='throne.Bathroom')),
            ],
            options={
            },
            bases=(models.Model,),
        )
    ]
