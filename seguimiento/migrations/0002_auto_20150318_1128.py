# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='tipo_doc',
            field=models.CharField(max_length=3, verbose_name=b'Tipo de documento', choices=[(b'EXP', b'Expediente'), (b'NOT', b'Nota'), (b'MEM', b'Memo')]),
        ),
    ]
