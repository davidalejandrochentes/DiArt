from django.contrib import admin
from .models import Footer, SocialLink


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    readonly_fields = ("logo_preview",)

    fieldsets = (
        (
            "Logo",
            {
                "fields": ("logo", "logo_preview"),
                "description": 'Si no se sube un logo, se mostrará el texto "DiArt"',
            },
        ),
        (
            "Información de contacto",
            {"fields": ("descripcion", "direccion", "telefono", "email", "horario")},
        ),
        ("Copyright", {"fields": ("copyright",)}),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return f'<img src="{obj.logo.url}" style="max-width: 150px; max-height: 50px;">'
        return "-"

    logo_preview.allow_tags = True
    logo_preview.short_description = "Vista previa"

    def has_add_permission(self, request):
        if Footer.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("plataforma", "url", "orden", "activo")
    list_filter = ("activo",)
    list_editable = ("orden", "activo")
    ordering = ("orden",)
