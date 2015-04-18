# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bah_api', '0002_auto_20150418_0018'),
    ]

    operations = [
        migrations.DeleteModel(
            name='withDependents',
        ),
    ]
