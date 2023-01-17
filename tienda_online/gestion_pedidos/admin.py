from django.contrib import admin
from gestion_pedidos.models import cliente,articulo,pedidos
# Register your models here.

class clientes_admin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "telefono")
    search_fields=("nombre","telefono")

class Articulos_admin(admin.ModelAdmin):
    list_filter=("seccion",)
    
class pedidos_admin(admin.ModelAdmin):
    list_display=("numero","fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha"

admin.site.register(cliente,clientes_admin)
admin.site.register(articulo,Articulos_admin)
admin.site.register(pedidos,pedidos_admin)
