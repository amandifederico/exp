# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0013_documento_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='proveedor',
            field=models.ForeignKey(db_column=b'proveedor', blank=True, to='seguimiento.Proveedor', null=True, verbose_name=b'proveedor'),
        ),
        migrations.AlterField(
            model_name='pase',
            name='observacion',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
