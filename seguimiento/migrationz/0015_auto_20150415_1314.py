# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0014_auto_20150414_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='adjunto',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='destino',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='proveedor',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='recepcion',
        ),
        migrations.RemoveField(
            model_name='documento',
            name='tipo_doc',
        ),
        migrations.DeleteModel(
            name='Notas',
        ),
        migrations.RemoveField(
            model_name='pase',
            name='destino',
        ),
        migrations.RemoveField(
            model_name='pase',
            name='documento',
        ),
        migrations.DeleteModel(
            name='Documento',
        ),
        migrations.RemoveField(
            model_name='pase',
            name='envio',
        ),
        migrations.RemoveField(
            model_name='pase',
            name='origen',
        ),
        migrations.DeleteModel(
            name='Departamento',
        ),
        migrations.RemoveField(
            model_name='pase',
            name='recepcion',
        ),
        migrations.DeleteModel(
            name='Pase',
        ),
        migrations.DeleteModel(
            name='Proveedor',
        ),
        migrations.DeleteModel(
            name='TipoDoc',
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
            ],
            options={
                'db_table': 'seguimiento_departamento',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
            ],
            options={
                'db_table': 'seguimiento_documento',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
            ],
            options={
                'db_table': 'seguimiento_notas',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pase',
            fields=[
            ],
            options={
                'db_table': 'seguimiento_pase',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
            ],
            options={
                'db_table': 'seguimiento_proveedor',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoDoc',
            fields=[
            ],
            options={
                'db_table': 'seguimiento_tipodoc',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
