# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bah_api', '0010_delete_zipmha'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZipMHA',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('ZipCode', models.CharField(max_length=5)),
                ('MHA', models.CharField(max_length=5)),
            ],
        ),
    ]
