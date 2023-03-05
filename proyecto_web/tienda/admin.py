from django.contrib import admin
from  .models import *
# Register your models here.


class CategoriaProd_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
class Producto_Admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(CategoriaProd,CategoriaProd_Admin)
admin.site.register(Producto,CategoriaProd_Admin)