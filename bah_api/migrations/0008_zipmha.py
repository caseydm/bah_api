# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bah_api', '0007_delete_zipmha'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZipMHA',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('ZipCode', models.CharField(max_length=5)),
                ('MHA', models.CharField(max_length=5)),
            ],
        ),
    ]
