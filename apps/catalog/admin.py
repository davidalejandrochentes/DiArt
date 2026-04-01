from django.contrib import admin
from .models import Category, GalleryImage


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1
    readonly_fields = ("imagen_preview",)
    fields = ("imagen", "imagen_preview", "orden", "activo")

    def imagen_preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" style="max-width: 100px; max-height: 100px; border-radius: 8px;">'
        return "-"

    imagen_preview.allow_tags = True
    imagen_preview.short_description = "Vista previa"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("titulo", "orden", "activo", "destacado", "imagen_preview")
    list_filter = ("activo", "destacado")
    list_editable = ("orden", "activo", "destacado")
    readonly_fields = ("slug", "imagen_preview")
    inlines = [GalleryImageInline]
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


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("categoria", "orden", "activo", "imagen_preview")
    list_filter = ("categoria", "activo")
    list_editable = ("orden", "activo")
    readonly_fields = ("imagen_preview",)
    ordering = ("categoria", "orden")

    def imagen_preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" style="max-width: 100px; max-height: 100px; border-radius: 8px;">'
        return "-"

    imagen_preview.allow_tags = True
    imagen_preview.short_description = "Vista previa"
