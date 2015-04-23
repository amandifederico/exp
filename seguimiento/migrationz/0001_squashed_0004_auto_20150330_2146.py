# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'seguimiento', '0001_initial'), (b'seguimiento', '0002_auto_20150318_1128'), (b'seguimiento', '0003_auto_20150330_2133'), (b'seguimiento', '0004_auto_20150330_2146')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
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
                ('envio', models.ForeignKey(related_name=b'envio', db_column=b'envio', default=None, blank=True, to=settings.AUTH_USER_MODEL)),
                ('recepcion', models.ForeignKey(related_name=b'recepcion', db_column=b'recepcion', default=None, blank=True, to=settings.AUTH_USER_MODEL)),
                ('recibido', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='documento',
            name='recepcion',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
