# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='status',
            field=models.CharField(default=b'Submitted', max_length=100, choices=[(b'Submitted', b'Submitted'), (b'Approved', b'Approved'), (b'Declined', b'Declined')]),
            preserve_default=True,
        ),
    ]
