# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seguimiento', '0003_auto_20150330_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='pase',
            name='envio',
            field=models.ForeignKey(related_name=b'envio', db_column=b'envio', default=None, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pase',
            name='recepcion',
            field=models.ForeignKey(related_name=b'recepcion', db_column=b'recepcion', default=None, blank=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pase',
            name='recibido',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='documento',
            name='recepcion',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
