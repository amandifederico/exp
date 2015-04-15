# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0005_auto_20150330_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='adjunto',
            field=models.ForeignKey(default=None, blank=True, to='seguimiento.Documento'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='recepcion',
            field=models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
