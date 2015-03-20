# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_squashed_0002_expense_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='receipt_image',
            field=models.ImageField(null=True, upload_to=b'expenses', blank=True),
        ),
    ]
