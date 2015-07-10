from django.contrib import admin

from models import *

#--------------------------------------------------------------------------------------------------------------------------------
class DetallePaseInline(admin.TabularInline):
     model = Pase
     raw_id_fields = ['documento']
     readonly_fields = ['documento','fecha_ing','motivo','envio','origen','destino','recepcion','observacion','recibido']
     
     def has_add_permission(self, request, obj=None):
        return False


# Register your models here.
class DocumentoAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['descripcion','tipo_doc','fecha_ing','destino','recepcion','adjunto']
    search_fields = ['descripcion','destino','recepcion','adjunto']
    list_filter = ['tipo_doc', 'recepcion','proveedor']
    readonly_fields = ['recepcion']
    raw_id_fields =['adjunto']

    inlines = [DetallePaseInline]
    
    def save_model(self, request, obj, form, change): 
        obj.recepcion = request.user
        obj.save()
#*******************************************************************************************************************************
class DetallePaseInlineMent(admin.TabularInline):
     model = VwPaseMesaEnt
     raw_id_fields = ('documento',)
     readonly_fields = ['documento','fecha_ing','motivo','envio','origen','destino','recepcion','observacion','recibido']
     
     def has_add_permission(self, request, obj=None):
        return False


# Register your models here.
class DocumentoMentAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['descripcion','nro','tipo_doc','fecha_ing','destino','recepcion','adjunto']
    search_fields = ['descripcion','nro']
    list_filter = ['tipo_doc', 'recepcion','proveedor']
    readonly_fields = ['recepcion']
    raw_id_fields =['adjunto']

    inlines = [DetallePaseInlineMent]
    
    def save_model(self, request, obj, form, change): 
        obj.recepcion = request.user
        obj.save()
#*******************************************************************************************************************************
class DetallePaseInlineDirec(admin.TabularInline):
     model = VwPaseDireccion
     raw_id_fields = ('documento',)
     readonly_fields = ['documento','fecha_ing','motivo','envio','origen','destino','recepcion','observacion','recibido']
     
     def has_add_permission(self, request, obj=None):
        return False


# Register your models here.
class DocumentoDirecAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['descripcion','nro','tipo_doc','fecha_ing','destino','recepcion','adjunto']
    search_fields = ['descripcion','nro']
    list_filter = ['tipo_doc', 'recepcion','proveedor']
    readonly_fields = ['recepcion']
    raw_id_fields =['adjunto']

    inlines = [DetallePaseInlineDirec]
    
    def save_model(self, request, obj, form, change): 
        obj.recepcion = request.user
        obj.save()
#*******************************************************************************************************************************
class DetallePaseInlineOtros(admin.TabularInline):
     model = VwPaseOtros
     raw_id_fields = ('documento',)
     readonly_fields = ['documento','fecha_ing','motivo','envio','origen','destino','recepcion','observacion','recibido']
     
     def has_add_permission(self, request, obj=None):
        return False


# Register your models here.
class DocumentoOtrosAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['descripcion','nro','tipo_doc','fecha_ing','destino','recepcion','adjunto']
    search_fields = ['descripcion','nro']
    list_filter = ['tipo_doc', 'recepcion','proveedor']
    readonly_fields = ['recepcion']
    raw_id_fields =['adjunto']

    inlines = [DetallePaseInlineOtros]
    
    def save_model(self, request, obj, form, change): 
        obj.recepcion = request.user
        obj.save()
#*******************************************************************************************************************************
class DetallePaseInlineTeso(admin.TabularInline):
     model = VwPaseTesoreria
     raw_id_fields = ('documento',)
     readonly_fields = ['documento','fecha_ing','motivo','envio','origen','destino','recepcion','observacion','recibido']
     
     def has_add_permission(self, request, obj=None):
        return False


# Register your models here.
class DocumentoTesoAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['descripcion','nro','tipo_doc','fecha_ing','destino','recepcion','adjunto']
    search_fields = ['descripcion','nro']
    list_filter = ['tipo_doc', 'recepcion','proveedor']
    readonly_fields = ['recepcion']
    raw_id_fields =['adjunto']

    inlines = [DetallePaseInlineTeso]
    
    def save_model(self, request, obj, form, change): 
        obj.recepcion = request.user
        obj.save()
#*******************************************************************************************************************************
class DetallePaseInlinePatri(admin.TabularInline):
     model = VwPasePatrimonio
     raw_id_fields = ('documento',)
     readonly_fields = ['documento','fecha_ing','motivo','envio','origen','destino','recepcion','observacion','recibido']
     
     def has_add_permission(self, request, obj=None):
        return False


# Register your models here.
class DocumentoPatriAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['descripcion','nro','tipo_doc','fecha_ing','destino','recepcion','adjunto']
    search_fields = ['descripcion','nro']
    list_filter = ['tipo_doc', 'recepcion','proveedor']
    readonly_fields = ['recepcion']
    raw_id_fields =['adjunto']

    inlines = [DetallePaseInlinePatri]
    
    def save_model(self, request, obj, form, change): 
        obj.recepcion = request.user
        obj.save()
#*******************************************************************************************************************************
class DetallePaseInlineLic(admin.TabularInline):
     model = VwPaseLicitacionCompras
     raw_id_fields = ('documento',)
     readonly_fields = ['documento','fecha_ing','motivo','envio','origen','destino','recepcion','observacion','recibido']
     
     def has_add_permission(self, request, obj=None):
        return False


# Register your models here.
class DocumentoLicAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['descripcion','nro','tipo_doc','fecha_ing','destino','recepcion','adjunto']
    search_fields = ['descripcion','nro']
    list_filter = ['tipo_doc', 'recepcion','proveedor']
    readonly_fields = ['recepcion']
    raw_id_fields =['adjunto']

    inlines = [DetallePaseInlineLic]
    
    def save_model(self, request, obj, form, change): 
        obj.recepcion = request.user
        obj.save()
#*******************************************************************************************************************************
class DetallePaseInlinePres(admin.TabularInline):
     model = VwPasePresupuesto
     raw_id_fields = ('documento',)
     readonly_fields = ['documento','fecha_ing','motivo','envio','origen','destino','recepcion','observacion','recibido']
     
     def has_add_permission(self, request, obj=None):
        return False


# Register your models here.
class DocumentoPresAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['descripcion','nro','tipo_doc','fecha_ing','destino','recepcion','adjunto']
    search_fields = ['descripcion','nro']
    list_filter = ['tipo_doc', 'recepcion','proveedor']
    readonly_fields = ['recepcion']
    raw_id_fields =['adjunto']

    inlines = [DetallePaseInlinePres]
    
    def save_model(self, request, obj, form, change): 
        obj.recepcion = request.user
        obj.save()
#*******************************************************************************************************************************


class NotasAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['nro','ejercicio','descripcion','direccion','usuario']
    search_fields = ['nro','direccion','usuario','descripcion']

class PaseAdmin(admin.ModelAdmin):
    list_display = ['documento','fecha_ing','motivo','envio','origen','destino','recepcion','observacion','recibido']
    #list_display = ['motivo','recibido','destino']
    raw_id_fields = ['documento']
    search_fields = ['documento__descripcion','documento__nro','origen__nombre','destino__nombre']
    def save_model(self, request, obj, form, change): 
        obj.envio = request.user
        obj.save()

    """def save_formset(self, request, form, formset, change): 
        if formset.model == Comment:
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        else:
            formset.save()
    """

    
#admin.site.register()
admin.site.register(Documento,DocumentoAdmin)
#admin.site.register(Expediente,DocumentoAdmin)
admin.site.register(VwDocumentoDireccion,DocumentoDirecAdmin)
admin.site.register(VwDocumentoMesaEnt,DocumentoMentAdmin)
admin.site.register(VwDocumentoOtros,DocumentoOtrosAdmin)
admin.site.register(VwDocumentoTesoreria,DocumentoTesoAdmin)
admin.site.register(VwDocumentoPatrimonio,DocumentoPatriAdmin)
admin.site.register(VwDocumentoLicitacionCompras,DocumentoLicAdmin)
admin.site.register(VwDocumentoPresupuesto,DocumentoPresAdmin)


#admin.site.register(Notas,NotasAdmin)
admin.site.register(Departamento)
#admin.site.register(TipoDoc)
admin.site.register(Proveedor)
admin.site.register(Pase,PaseAdmin)
admin.site.register(VwPaseOtros,PaseAdmin)
admin.site.register(VwPaseTesoreria,PaseAdmin)
admin.site.register(VwPaseMesaEnt,PaseAdmin)
admin.site.register(VwPasePatrimonio,PaseAdmin)
admin.site.register(VwPaseLicitacionCompras,PaseAdmin)
admin.site.register(VwPasePresupuesto,PaseAdmin)
admin.site.register(VwPaseDireccion,PaseAdmin)

admin.site.register(VwPaseOtrosS,PaseAdmin)
admin.site.register(VwPaseTesoreriaS,PaseAdmin)
admin.site.register(VwPaseMesaEntS,PaseAdmin)
admin.site.register(VwPasePatrimonioS,PaseAdmin)
admin.site.register(VwPaseLicitacionComprasS,PaseAdmin)
admin.site.register(VwPasePresupuestoS,PaseAdmin)
admin.site.register(VwPaseDireccionS,PaseAdmin)
