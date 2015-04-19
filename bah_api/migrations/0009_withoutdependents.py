# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bah_api', '0008_zipmha'),
    ]

    operations = [
        migrations.CreateModel(
            name='withOutDependents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('MHA', models.CharField(max_length=5)),
                ('E1', models.DecimalField(max_digits=10, decimal_places=2)),
                ('E2', models.DecimalField(max_digits=10, decimal_places=2)),
                ('E3', models.DecimalField(max_digits=10, decimal_places=2)),
                ('E4', models.DecimalField(max_digits=10, decimal_places=2)),
                ('E5', models.DecimalField(max_digits=10, decimal_places=2)),
                ('E6', models.DecimalField(max_digits=10, decimal_places=2)),
                ('E7', models.DecimalField(max_digits=10, decimal_places=2)),
                ('E8', models.DecimalField(max_digits=10, decimal_places=2)),
                ('E9', models.DecimalField(max_digits=10, decimal_places=2)),
                ('W1', models.DecimalField(max_digits=10, decimal_places=2)),
                ('W2', models.DecimalField(max_digits=10, decimal_places=2)),
                ('W3', models.DecimalField(max_digits=10, decimal_places=2)),
                ('W4', models.DecimalField(max_digits=10, decimal_places=2)),
                ('W5', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O1E', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O2E', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O3E', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O1', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O2', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O3', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O4', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O5', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O6', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O7', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O8', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O9', models.DecimalField(max_digits=10, decimal_places=2)),
                ('O10', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
    ]
