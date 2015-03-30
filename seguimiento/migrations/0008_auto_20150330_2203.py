# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0007_auto_20150330_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='recepcion',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
