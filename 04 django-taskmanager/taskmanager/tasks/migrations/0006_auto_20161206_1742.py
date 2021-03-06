# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-06 14:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20161206_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[(b'T', b'To Do'), (b'P', b'In Progress'), (b'R', b'Review'), (b'D', b'Done')], default=b'T', max_length=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime.today, null=True),
        ),
    ]
