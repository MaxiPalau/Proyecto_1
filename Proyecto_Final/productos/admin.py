from django.contrib import admin
from productos.models import Productos, Marcas, Tipo, Distribuidores, Distribuidores_Marcas

# Register your models here.

admin.site.register(Tipo)

class Display_marcas(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')

admin.site.register(Marcas, Display_marcas)

class Display_productos(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'modelo', 'sku', 'tipo', 'stock', 'precio')

admin.site.register(Productos, Display_productos)

class Display_distribuidores(admin.ModelAdmin):
    list_display = ('razon_social', 'direccion', 'localidad', 'pais', 'telefono', 'mail', 'web', 'cuit', 'descripcion')

admin.site.register(Distribuidores, Display_distribuidores)

class Display_dist_marcas(admin.ModelAdmin):
    list_display = ('marca', 'distribuidor')
    
admin.site.register(Distribuidores_Marcas, Display_dist_marcas)