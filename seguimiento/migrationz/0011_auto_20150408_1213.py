# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0010_auto_20150330_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idprov', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoDoc',
            fields=[
                ('idtdoc', models.AutoField(serialize=False, primary_key=True)),
                ('descrip', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='documento',
            name='tipo_doc',
            field=models.ForeignKey(db_column=b'tipo_doc', verbose_name=b'Tipo Documento', to='seguimiento.TipoDoc'),
        ),
    ]
