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
#///////////////////////////////////////////////////////////////////
class Proveedor(models.Model):
    idprov = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300)
    direccion = models.CharField(max_length=300, null=True)

    def __unicode__(self):
        return force_unicode(self.nombre)

    class Meta:
        app_label = 'seguimiento'
        managed = False
        db_table = 'seguimiento_proveedor'

#///////////////////////////////////////////////////////////////////
class TipoDoc(models.Model):
    idtdoc = models.AutoField(primary_key=True)
    descrip = models.CharField(max_length=300)

    def __unicode__(self):
        return force_unicode(self.descrip)

    class Meta:
        app_label = 'seguimiento'
        managed = False
        db_table = 'seguimiento_tipodoc'

#///////////////////////////////////////////////////////////////////
class Departamento(models.Model):
    iddep = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=300)
    
    def __unicode__(self):
        return force_unicode(self.nombre)

    class Meta:
        app_label = 'seguimiento'
        managed = False
        db_table = 'seguimiento_departamento'

#///////////////////////////////////////////////////////////////////
class Documento(models.Model):
    iddoc = models.AutoField(primary_key=True)
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    tipo_doc = models.ForeignKey(TipoDoc,db_column='tipo_doc',verbose_name= "Tipo Documento")
    nro = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=300)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino")
    proveedor = models.ForeignKey(Proveedor,db_column='proveedor',verbose_name= "proveedor", null=True, blank=True)
    recepcion = models.ForeignKey(User,db_column='recepcion', blank=True, null=True)
    adjunto = models.ForeignKey('self', db_column='adjunto', blank=True, default= None, null=True)
    
    def __unicode__(self):
        return force_unicode(self.descripcion)

    class Meta:
        app_label = 'seguimiento'
        managed = False
        db_table = 'seguimiento_documento'
        
#///////////////////////////////////////////////////////////////////
class Pase(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(Documento,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='envio', blank=True, null=True, default=None)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="origen", related_query_name="origen")
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="destino", related_query_name="destino")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='recepcion',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)
    
    def __unicode__(self):
        return force_unicode(self.motivo)
    
    class Meta:
        app_label = 'seguimiento'
        managed = False
        db_table = 'seguimiento_pase'


#=======================================================================================================
#Otros
#=======================================================================================================
class VwDocumentoOtros(models.Model):
    iddoc = models.AutoField(primary_key=True)
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    tipo_doc = models.ForeignKey(TipoDoc,db_column='tipo_doc',verbose_name= "Tipo Documento")
    nro = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=200)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino", default=1, editable=False)
    proveedor = models.ForeignKey(Proveedor,db_column='proveedor',verbose_name= "proveedor", null=True, blank=True)
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='doc_otros_recepcion',blank=True, null=True, default=None)
    adjunto = models.ForeignKey('self', db_column='adjunto', blank=True, default= None, null=True)

    def __unicode__(self):
        return force_unicode(self.descripcion)

    class Meta:
        managed = False
        verbose_name = "Documento Otros"
        db_table = 'vw_documento_otros'

class VwPaseOtros(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoOtros,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='otros_envio', blank=True, null=True, default=None)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="otros_origen", related_query_name="otros_origen", default=1, editable=False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="otros_destino", related_query_name="otros_destino")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='pase_otros_recepcion',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)
    
    def __unicode__(self):
        return force_unicode(self.motivo)
    
    class Meta:
        managed = False
        verbose_name = "Pase Otros ENTRADA"
        db_table = 'vw_pase_otros'

class VwPaseOtrosS(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoOtros,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='otros_envio_s', blank=True, null=True, default=None)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="otros_origen_s", related_query_name="otros_origen_s", default=1, editable=False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="otros_destino_s", related_query_name="otros_destino_s")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='pase_otros_recepcion_s',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)
    
    def __unicode__(self):
        return force_unicode(self.motivo)
    
    class Meta:
        managed = False
        verbose_name = "Pase Otros SALIDA"
        db_table = 'vw_pase_otros_s'

#=======================================================================================================
#Tesoreria
#=======================================================================================================
class VwDocumentoTesoreria(models.Model):
    iddoc = models.AutoField(primary_key=True)
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    tipo_doc = models.ForeignKey(TipoDoc,db_column='tipo_doc',verbose_name= "Tipo Documento")
    nro = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=200)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino", default=2, editable=False)
    proveedor = models.ForeignKey(Proveedor,db_column='proveedor',verbose_name= "proveedor", null=True, blank=True)
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='doc_teso_recepcion',blank=True, null=True, default=None)
    adjunto = models.ForeignKey('self', db_column='adjunto', blank=True, default= None, null=True)

    def __unicode__(self):
        return force_unicode(self.descripcion)

    class Meta:
        managed = False
        verbose_name = "Documento Tesoreria"
        db_table = 'vw_documento_tesoreria'

class VwPaseTesoreria(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoTesoreria,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='tesoreria_envio', blank=True, null=True, default=None)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="tesoreria_origen", related_query_name="tesoreria_origen",default=2, editable=False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="tesoreria_destino", related_query_name="tesoreria_destino")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='tesoreria_recepcion',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)

    def __unicode__(self):
        return force_unicode(self.motivo)

    class Meta:
        managed = False
        verbose_name = "Pase Tesoreria ENTRADA"
        db_table = 'vw_pase_tesoreria'

class VwPaseTesoreriaS(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoTesoreria,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='tesoreria_envio_s', blank=True, null=True, default=None)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="tesoreria_origen_s", related_query_name="tesoreria_origen_s",default=2, editable=False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="tesoreria_destino_s", related_query_name="tesoreria_destino_s")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='tesoreria_recepcion_s',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)

    def __unicode__(self):
        return force_unicode(self.motivo)

    class Meta:
        managed = False
        verbose_name = "Pase Tesoreria SALIDA"
        db_table = 'vw_pase_tesoreria_s'
#=======================================================================================================
#Mesa de entrada
#=======================================================================================================
class VwDocumentoMesaEnt(models.Model):
    iddoc = models.AutoField(primary_key=True)
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    tipo_doc = models.ForeignKey(TipoDoc,db_column='tipo_doc',verbose_name= "Tipo Documento")
    nro = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=200)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino", default= 3, editable=False)
    proveedor = models.ForeignKey(Proveedor,db_column='proveedor',verbose_name= "proveedor", null=True, blank=True)
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='doc_mesa_ent_recepcion',blank=True, null=True, default=None)
    adjunto = models.ForeignKey('self', db_column='adjunto', blank=True, default= None, null=True)

    def __unicode__(self):
        return force_unicode(self.descripcion)
	
    class Meta:
        verbose_name = "Documento Mesa de Entrada"
        managed = False
        db_table = 'vw_documento_mesa_ent'

class VwPaseMesaEnt(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoMesaEnt,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='mesa_ent_envio', blank=True, null=True, default=None, editable=False)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="mesa_ent_origen", related_query_name="mesa_ent_origen", default=3, editable=False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="mesa_ent_destino", related_query_name="mesa_ent_destino")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='mesa_ent_recepcion',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)

    def __unicode__(self):
        return force_unicode(self.documento)

    class Meta:
        verbose_name = "Pase Mesa Entrada ENTRADA"
        managed = False
        #db_table = 'vw_pase_mesa_ent'
        db_table = 'vw_pase_mesa_ent'
        
class VwPaseMesaEntS(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoMesaEnt,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='mesa_ent_envio_s', blank=True, null=True, default=None, editable=False)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="mesa_ent_origen_s", related_query_name="mesa_ent_origen_s", default=3, editable=False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="mesa_ent_destino_s", related_query_name="mesa_ent_destino_s")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='mesa_ent_recepcion_s',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)

    def __unicode__(self):
        return force_unicode(self.documento)

    class Meta:
        verbose_name = "Pase Mesa Entrada SALIDA"
        managed = False
        #db_table = 'vw_pase_mesa_ent'
        db_table = 'vw_pase_mesa_ent_s'
#=======================================================================================================
#Direccion
#=======================================================================================================
class VwDocumentoDireccion(models.Model):
    iddoc = models.AutoField(primary_key=True)
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    tipo_doc = models.ForeignKey(TipoDoc,db_column='tipo_doc',verbose_name= "Tipo Documento")
    nro = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=200)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino", default=7, editable=False)
    proveedor = models.ForeignKey(Proveedor,db_column='proveedor',verbose_name= "proveedor", null=True, blank=True)
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='doc_direccion_recepcion',blank=True, null=True, default=None)
    adjunto = models.ForeignKey('self', db_column='adjunto', blank=True, default= None, null=True)

    def __unicode__(self):
        return force_unicode(self.descripcion)
	
    class Meta:
        verbose_name = "Documento Direccion"
        managed = False
        db_table = 'vw_documento_direccion'

class VwPaseDireccion(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoDireccion,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='direccion_envio', blank=True, null=True, default=None, editable=False)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="direccion_origen", related_query_name="direccion_origen",default=7, editable=False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="direccion_destino", related_query_name="direccion_destino")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='direccion_recepcion',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)

    def __unicode__(self):
        return force_unicode(self.motivo)

    class Meta:
        verbose_name = "Pase Direccion ENTRADA"
        managed = False
        #db_table = 'vw_pase_direccion'
        db_table = 'vw_pase_direccion'
        
class VwPaseDireccionS(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoDireccion,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='direccion_envio_s', blank=True, null=True, default=None, editable=False)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="direccion_origen_s", related_query_name="direccion_origen_s",default=7, editable=False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="direccion_destino_s", related_query_name="direccion_destino_s")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='direccion_recepcion_s',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)

    def __unicode__(self):
        return force_unicode(self.motivo)

    class Meta:
        verbose_name = "Pase Direccion SALIDA"
        managed = False
        #db_table = 'vw_pase_direccion'
        db_table = 'vw_pase_direccion_s'
#=======================================================================================================
#Patrimonio
#=======================================================================================================
class VwDocumentoPatrimonio(models.Model):
    iddoc = models.AutoField(primary_key=True)
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    tipo_doc = models.ForeignKey(TipoDoc,db_column='tipo_doc',verbose_name= "Tipo Documento")
    nro = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=200)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino", default=6, editable=False)
    proveedor = models.ForeignKey(Proveedor,db_column='proveedor',verbose_name= "proveedor", null=True, blank=True)
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='doc_patrimonio_recepcion',blank=True, null=True, default=None)
    adjunto = models.ForeignKey('self', db_column='adjunto', blank=True, default= None, null=True)

    def __unicode__(self):
        return force_unicode(self.descripcion)

    class Meta:
        managed = False
        verbose_name = "Documento Patrimonio"
        db_table = 'vw_documento_patrimonio'

class VwPasePatrimonio(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoPatrimonio,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='patrimonio_envio', blank=True, null=True, default=None)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="patrimonio_origen", related_query_name="patrimonio_origen",default=6, editable= False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="patrimonio_destino", related_query_name="patrimonio_destino")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='patrimonio_recepcion',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)

    def __unicode__(self):
        return force_unicode(self.motivo)

    class Meta:
        managed = False
        db_table = 'vw_pase_patrimonio'
        verbose_name = "Pase Patrimonio ENTRADA"

class VwPasePatrimonioS(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoPatrimonio,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='patrimonio_envio_s', blank=True, null=True, default=None)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="patrimonio_origen_s", related_query_name="patrimonio_origen_s",default=6, editable= False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="patrimonio_destino_s", related_query_name="patrimonio_destino_s")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='patrimonio_recepcion_s',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)

    def __unicode__(self):
        return force_unicode(self.motivo)

    class Meta:
        managed = False
        db_table = 'vw_pase_patrimonio_s'
        verbose_name = "Pase Patrimonio SALIDA"

#=======================================================================================================
#Licitacion y compras
#=======================================================================================================
class VwDocumentoLicitacionCompras(models.Model):
    iddoc = models.AutoField(primary_key=True)
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    tipo_doc = models.ForeignKey(TipoDoc,db_column='tipo_doc',verbose_name= "Tipo Documento")
    nro = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=200)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino", default=5, editable=False)
    proveedor = models.ForeignKey(Proveedor,db_column='proveedor',verbose_name= "proveedor", null=True, blank=True)
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='doc_lic_com_recepcion',blank=True, null=True, default=None)
    adjunto = models.ForeignKey('self', db_column='adjunto', blank=True, default= None, null=True)

    def __unicode__(self):
        return force_unicode(self.descripcion)

    class Meta:
        managed = False
        verbose_name = "Documento Licitacion y Compras"
        db_table = 'vw_documento_lic_com'

class VwPaseLicitacionCompras(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoLicitacionCompras,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='lic_com_envio', blank=True, null=True, default=None)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="lic_com_origen", related_query_name="lic_com_origen",default=5, editable=False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="lic_com_destino", related_query_name="lic_com_destino")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='lic_com_recepcion',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)

    def __unicode__(self):
        return force_unicode(self.motivo)

    class Meta:
        managed = False
        db_table = 'vw_pase_lic_com'
        verbose_name = "Pase Licitacion y Compras ENTRADA"

class VwPaseLicitacionComprasS(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoLicitacionCompras,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='lic_com_envio_s', blank=True, null=True, default=None)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="lic_com_origen_s", related_query_name="lic_com_origen_s",default=5, editable=False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="lic_com_destino_s", related_query_name="lic_com_destino_s")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='lic_com_recepcion_s',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)

    def __unicode__(self):
        return force_unicode(self.motivo)

    class Meta:
        managed = False
        db_table = 'vw_pase_lic_com_s'
        verbose_name = "Pase Licitacion y Compras SALIDA"
#=======================================================================================================
#Ejecucion Presupuestaria
#=======================================================================================================
class VwDocumentoPresupuesto(models.Model):
    iddoc = models.AutoField(primary_key=True)
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    tipo_doc = models.ForeignKey(TipoDoc,db_column='tipo_doc',verbose_name= "Tipo Documento")
    nro = models.CharField(max_length=200, null=True)
    descripcion = models.CharField(max_length=200)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino", default=4, editable=False)
    proveedor = models.ForeignKey(Proveedor,db_column='proveedor',verbose_name= "proveedor", null=True, blank=True)
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='doc_presupuesto_recepcion',blank=True, null=True, default=None)
    adjunto = models.ForeignKey('self', db_column='adjunto', blank=True, default= None, null=True)

    def __unicode__(self):
        return force_unicode(self.descripcion)

    class Meta:
        managed = False
        verbose_name = "Documento Presupuesto"
        db_table = 'vw_documento_presupuesto'

class VwPasePresupuesto(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoPresupuesto,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='presupuesto_envio', blank=True, null=True, default=None)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="presupuesto_origen", related_query_name="presupuesto_origen",default=4, editable=False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="presupuesto_destino", related_query_name="presupuesto_destino")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='presupuesto_recepcion',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)

    def __unicode__(self):
        return force_unicode(self.motivo)

    class Meta:
        managed = False
        db_table = 'vw_pase_presupuesto'
        verbose_name = "Pase Presupuesto ENTRADA"

class VwPasePresupuestoS(models.Model):
    idpase = models.AutoField(primary_key=True)
    documento = models.ForeignKey(VwDocumentoPresupuesto,db_column='documento',verbose_name= "Documento")
    fecha_ing = models.DateField(verbose_name= "Fecha de Ingreso")
    motivo = models.CharField(max_length=200)
    envio = models.ForeignKey(User, db_column='envio', related_name='presupuesto_envio_s', blank=True, null=True, default=None)
    origen = models.ForeignKey(Departamento,db_column='origen',verbose_name= "Origen", related_name="presupuesto_origen_s", related_query_name="presupuesto_origen_s",default=4, editable=False)
    destino = models.ForeignKey(Departamento,db_column='destino',verbose_name= "Destino",related_name="presupuesto_destino_s", related_query_name="presupuesto_destino_s")
    recepcion = models.ForeignKey(User, db_column='recepcion', related_name='presupuesto_recepcion_s',blank=True, null=True, default=None)
    observacion = models.CharField(max_length=200,blank=True, null=True)
    recibido = models.BooleanField(default=False)

    def __unicode__(self):
        return force_unicode(self.motivo)

    class Meta:
        managed = False
        db_table = 'vw_pase_presupuesto_s'
        verbose_name = "Pase Presupuesto SALIDA"
