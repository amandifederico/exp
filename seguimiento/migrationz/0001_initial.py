# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('identr', models.AutoField(serialize=False, primary_key=True)),
                ('fecha_ing', models.DateField(verbose_name=b'Fecha de Ingreso')),
                ('tipo_doc', models.CharField(max_length=1, verbose_name=b'Tipo de documento', choices=[(b'EXP', b'Expediente'), (b'NOT', b'Nota'), (b'MEM', b'Memo')])),
                ('descripcion', models.CharField(max_length=200)),
                ('destino', models.CharField(max_length=3, verbose_name=b'Destino', choices=[(b'COM', b'Compras'), (b'SG', b'Secretaria General'), (b'SUE', b'Sueldos')])),
                ('recepcion', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('idnot', models.AutoField(serialize=False, primary_key=True)),
                ('nro', models.IntegerField()),
                ('ejercicio', models.IntegerField()),
                ('direccion', models.CharField(max_length=3, verbose_name=b'Destino', choices=[(b'COM', b'Compras'), (b'SG', b'Secretaria General'), (b'SUE', b'Sueldos')])),
                ('usuario', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
