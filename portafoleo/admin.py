from django.contrib import admin
from .models import Portafolio, CategoriaPortafolio, ImagenCategoria


@admin.register(Portafolio)
class PortafolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion', 'activo']
    list_editable = ['activo']


class ImagenCategoriaInline(admin.TabularInline):
    model = ImagenCategoria
    extra = 1
    fields = ['imagen', 'orden', 'activo']


@admin.register(CategoriaPortafolio)
class CategoriaPortafolioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug', 'orden', 'activo']
    list_editable = ['orden', 'activo']
    prepopulated_fields = {'slug': ['nombre']}
    inlines = [ImagenCategoriaInline]


@admin.register(ImagenCategoria)
class ImagenCategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoria', 'orden', 'activo']
    list_filter = ['categoria', 'activo']
    list_editable = ['orden', 'activo']
    raw_id_fields = ['categoria']
