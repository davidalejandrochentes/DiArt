from django.contrib import admin
from .models import Tienda, CategoriaTienda, Producto


@admin.register(Tienda)
class TiendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'activo']
    list_editable = ['activo']


class ProductoInline(admin.TabularInline):
    model = Producto
    extra = 1
    fields = ['nombre', 'slug', 'descripcion', 'precio_normal', 'precio_rebajado', 'imagen', 'orden', 'activo']


@admin.register(CategoriaTienda)
class CategoriaTiendaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'orden', 'activo']
    list_editable = ['orden', 'activo']
    prepopulated_fields = {'slug': ['nombre']}
    inlines = [ProductoInline]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio_normal', 'precio_rebajado', 'orden', 'activo']
    list_filter = ['categoria', 'activo']
    list_editable = ['orden', 'activo']
    prepopulated_fields = {'slug': ['nombre']}
    raw_id_fields = ['categoria']
