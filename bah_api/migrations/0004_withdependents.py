# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bah_api', '0003_delete_withdependents'),
    ]

    operations = [
        migrations.CreateModel(
            name='withDependents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MHA', models.CharField(max_length=5)),
                ('E1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('E2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('E3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('E4', models.DecimalField(decimal_places=2, max_digits=10)),
                ('E5', models.DecimalField(decimal_places=2, max_digits=10)),
                ('E6', models.DecimalField(decimal_places=2, max_digits=10)),
                ('E7', models.DecimalField(decimal_places=2, max_digits=10)),
                ('E8', models.DecimalField(decimal_places=2, max_digits=10)),
                ('E9', models.DecimalField(decimal_places=2, max_digits=10)),
                ('W1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('W2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('W3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('W4', models.DecimalField(decimal_places=2, max_digits=10)),
                ('W5', models.DecimalField(decimal_places=2, max_digits=10)),
                ('O1E', models.DecimalField(decimal_places=2, max_digits=10)),
                ('O2E', models.DecimalField(decimal_places=2, max_digits=10)),
                ('O3E', models.DecimalField(decimal_places=2, max_digits=10)),
                ('O1', models.DecimalField(decimal_places=2, max_digits=10)),
                ('O2', models.DecimalField(decimal_places=2, max_digits=10)),
                ('O3', models.DecimalField(decimal_places=2, max_digits=10)),
                ('O4', models.DecimalField(decimal_places=2, max_digits=10)),
                ('O5', models.DecimalField(decimal_places=2, max_digits=10)),
                ('O6', models.DecimalField(decimal_places=2, max_digits=10)),
                ('O7', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
