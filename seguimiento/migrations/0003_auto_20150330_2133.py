# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0002_auto_20150318_1128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('iddep', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('identr', models.AutoField(serialize=False, primary_key=True)),
                ('fecha_ing', models.DateField(verbose_name=b'Fecha de Ingreso')),
                ('tipo_doc', models.CharField(max_length=3, verbose_name=b'Tipo de documento', choices=[(b'EXP', b'Expediente'), (b'NOT', b'Nota'), (b'MEM', b'Memo'), (b'FAC', b'Factura')])),
                ('descripcion', models.CharField(max_length=200)),
                ('destino', models.CharField(max_length=3, verbose_name=b'Destino', choices=[(b'COM', b'Compras'), (b'SG', b'Secretaria General'), (b'SUE', b'Sueldos')])),
                ('recepcion', models.CharField(max_length=200)),
                ('adjunto', models.ForeignKey(to='seguimiento.Documento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pase',
            fields=[
                ('idpase', models.AutoField(serialize=False, primary_key=True)),
                ('fecha_ing', models.DateField(verbose_name=b'Fecha de Ingreso')),
                ('motivo', models.CharField(max_length=200)),
                ('observacion', models.CharField(max_length=200)),
                ('destino', models.ForeignKey(related_query_name=b'destino', related_name=b'destino', db_column=b'destino', verbose_name=b'Destino', to='seguimiento.Departamento')),
                ('documento', models.ForeignKey(db_column=b'identr', verbose_name=b'Documento', to='seguimiento.Documento')),
                ('origen', models.ForeignKey(related_query_name=b'origen', related_name=b'origen', db_column=b'origen', verbose_name=b'Origen', to='seguimiento.Departamento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Entrada',
        ),
    ]
