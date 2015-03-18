from django.contrib import admin

from models import *

# Register your models here.
class EntradaAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['descripcion','tipo_doc','fecha_ing','destino','recepcion']
    search_fields = ['descripcion','destino','recepcion']

class NotasAdmin(admin.ModelAdmin):
    #raw_id_fields = []
    list_display = ['nro','ejercicio','descripcion','direccion','usuario']
    search_fields = ['nro','direccion','usuario','descripcion']

#admin.site.register()
admin.site.register(Entrada,EntradaAdmin)
admin.site.register(Notas,NotasAdmin)
