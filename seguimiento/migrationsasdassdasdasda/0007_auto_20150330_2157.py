# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0006_auto_20150330_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='adjunto',
            field=models.ForeignKey(default=None, blank=True, to='seguimiento.Documento', null=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='recepcion',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
