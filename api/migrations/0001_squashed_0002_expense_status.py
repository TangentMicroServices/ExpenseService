# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [(b'api', '0001_initial'), (b'api', '0002_expense_status')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=200, db_index=True)),
                ('project', models.CharField(default=None, max_length=200, db_index=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(verbose_name=b'Start Date', db_index=True)),
                ('receipt_image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('status', models.CharField(default=b'Submitted', max_length=100, choices=[(b'Submitted', b'Submitted'), (b'Approved', b'Approved'), (b'Declined', b'Declined')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
