from django.db import models
from django.utils.encoding import force_unicode
# Create your models here.

TIPO_DOCUMENTO = (
        ("EXP","Expediente"),
	("NOT","Nota"),
	("MEM","Memo"),
)

TIPO_DIRECCION = (
        ("COM","Compras"),
	("SG","Secretaria General"),
	("SUE","Sueldos"),
)

class Entrada(models.Model):
    identr = models.AutoField(primary_key=True)
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    tipo_doc = models.CharField(max_length=3, choices=TIPO_DOCUMENTO, verbose_name='Tipo de documento')
    descripcion = models.CharField(max_length=200)
    destino = models.CharField(max_length=3, choices=TIPO_DIRECCION, verbose_name='Destino')
    recepcion = models.CharField(max_length=200)
    
    def __unicode__(self):
        return force_unicode(self.descripcion)

class Notas(models.Model):
    idnot = models.AutoField(primary_key=True)
    nro = models.IntegerField()
    ejercicio = models.IntegerField()
    direccion = models.CharField(max_length=3, choices=TIPO_DIRECCION, verbose_name='Destino')
    usuario = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

    def __unicode__(self):
        return force_unicode(self.descripcion)
