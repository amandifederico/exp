# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0004_auto_20150330_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='adjunto',
            field=models.ForeignKey(to='seguimiento.Documento', blank=True),
        ),
        migrations.AlterField(
            model_name='documento',
            name='recepcion',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
