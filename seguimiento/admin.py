from django.contrib import admin

from models import *

# Register your models here.
class DocumentoAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['descripcion','tipo_doc','fecha_ing','destino','recepcion','adjunto']
    search_fields = ['descripcion','destino','recepcion','adjunto']
    list_filter = ['tipo_doc', 'recepcion','proveedor']
    readonly_fields = ['recepcion']
    raw_id_fields =['adjunto']
    
    def save_model(self, request, obj, form, change): 
        obj.recepcion = request.user
        obj.save()

class NotasAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['nro','ejercicio','descripcion','direccion','usuario']
    search_fields = ['nro','direccion','usuario','descripcion']

class PaseAdmin(admin.ModelAdmin):
    list_display = ['documento','fecha_ing','motivo','envio','origen','destino','recepcion','observacion','recibido']
    raw_id_fields = ['documento']
    search_fields = ['documento','destino','envio','destino','recepcion']
    def save_model(self, request, obj, form, change): 
        obj.user = request.user
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
admin.site.register(VwDocumentoContaduria,DocumentoAdmin)
admin.site.register(Notas,NotasAdmin)
admin.site.register(Departamento)
admin.site.register(TipoDoc)
admin.site.register(Proveedor)
admin.site.register(Pase,PaseAdmin)
admin.site.register(VwPaseContaduria,PaseAdmin)
