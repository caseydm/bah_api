# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bah_api', '0006_withdependents'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ZipMHA',
        ),
    ]
