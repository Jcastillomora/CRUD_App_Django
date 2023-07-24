from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto


# Register your models here.+
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display_links = ['nombre']

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    list_display_links = ['nombre', 'laboratorio']

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre','laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_display_links = ['nombre', 'laboratorio']
    ordering = ('nombre', 'laboratorio')
    list_filter = ('nombre', 'laboratorio')

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)




   



