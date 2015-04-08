# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0012_auto_20150408_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='proveedor',
            field=models.ForeignKey(db_column=b'proveedor', verbose_name=b'proveedor', to='seguimiento.Proveedor', null=True),
            preserve_default=True,
        ),
    ]
