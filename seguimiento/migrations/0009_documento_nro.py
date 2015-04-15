# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0008_auto_20150330_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='nro',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
