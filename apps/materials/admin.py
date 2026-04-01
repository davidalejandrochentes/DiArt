from django.contrib import admin
from .models import MaterialCategory, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1
    readonly_fields = ("slug", "imagen_preview")
    fields = (
        "nombre",
        "slug",
        "descripcion",
        "imagen",
        "imagen_preview",
        "orden",
        "activo",
    )

    def imagen_preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" style="max-width: 100px; max-height: 100px; border-radius: 8px;">'
        return "-"

    imagen_preview.allow_tags = True
    imagen_preview.short_description = "Vista previa"


@admin.register(MaterialCategory)
class MaterialCategoryAdmin(admin.ModelAdmin):
    list_display = ("titulo", "orden", "activo", "destacado", "imagen_preview")
    list_filter = ("activo", "destacado")
    list_editable = ("orden", "activo", "destacado")
    readonly_fields = ("slug", "imagen_preview")
    inlines = [ProductInline]
    ordering = ("orden",)

    fieldsets = (
        ("Información", {"fields": ("titulo", "slug", "descripcion")}),
        ("Multimedia", {"fields": ("imagen", "imagen_preview")}),
        ("Configuración", {"fields": ("orden", "activo", "destacado")}),
    )

    def imagen_preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" style="max-width: 150px; max-height: 150px; border-radius: 8px;">'
        return "-"

    imagen_preview.allow_tags = True
    imagen_preview.short_description = "Vista previa"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "orden", "activo", "imagen_preview")
    list_filter = ("categoria", "activo")
    list_editable = ("orden", "activo")
    readonly_fields = ("slug", "imagen_preview")
    ordering = ("categoria", "orden")

    fieldsets = (
        ("Información", {"fields": ("categoria", "nombre", "slug", "descripcion")}),
        ("Multimedia", {"fields": ("imagen", "imagen_preview")}),
        ("Configuración", {"fields": ("orden", "activo")}),
    )

    def imagen_preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" style="max-width: 150px; max-height: 150px; border-radius: 8px;">'
        return "-"

    imagen_preview.allow_tags = True
    imagen_preview.short_description = "Vista previa"
