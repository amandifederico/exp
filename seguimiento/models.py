from django.db import models
from django.utils.encoding import force_unicode
from django.contrib.auth.models import User
# Create your models here.

TIPO_DOCUMENTO = (
    ("EXP","Expediente"),
    ("NOT","Nota"),
    ("MEM","Memo"),
    ("FAC","Factura"),
)

TIPO_DIRECCION = (
    ("COM","Compras"),
    ("SG","Secretaria General"),
    ("SUE","Sueldos"),
)

class Documento(models.Model):
    identr = models.AutoField(primary_key=True)
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    tipo_doc = models.CharField(max_length=3, choices=TIPO_DOCUMENTO, verbose_name='Tipo de documento')
    nro = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=200)
    destino = models.CharField(max_length=3, choices=TIPO_DIRECCION, verbose_name='Destino')
    recepcion = models.ForeignKey(User, blank=True, null=True)
    adjunto = models.ForeignKey('self', blank=True, default= None, null=True)
    
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

class Departamento(models.Model):
    iddep = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return force_unicode(self.nombre)

class Pase(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(Documento,db_column='identr',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='envio', blank=True, null=True, default=None)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="origen", related_query_name="origen")
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="destino", related_query_name="destino")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='recepcion',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200)
    recibido = models.BooleanField(default=False)
    
    def __unicode__(self):
        return force_unicode(self.motivo)