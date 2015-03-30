# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0009_documento_nro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pase',
            name='envio',
            field=models.ForeignKey(related_name=b'envio', db_column=b'envio', default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='pase',
            name='recepcion',
            field=models.ForeignKey(related_name=b'recepcion', db_column=b'recepcion', default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
