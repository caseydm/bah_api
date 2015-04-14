# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BAH',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('rank', models.CharField(max_length=4)),
                ('dependents', models.BooleanField()),
                ('MHA', models.CharField(max_length=5)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
    ]
