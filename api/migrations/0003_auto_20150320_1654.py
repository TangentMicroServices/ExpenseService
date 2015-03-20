# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150320_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Start Date', db_index=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
