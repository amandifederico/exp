# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0011_auto_20150408_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='destino',
            field=models.ForeignKey(db_column=b'destino', verbose_name=b'Destino', to='seguimiento.Departamento'),
        ),
    ]
