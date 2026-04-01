from django.contrib import admin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cargo", "orden", "activo", "imagen_preview")
    list_filter = ("activo",)
    list_editable = ("orden", "activo")
    readonly_fields = ("imagen_preview",)
    ordering = ("orden",)

    fieldsets = (
        ("Información", {"fields": ("nombre", "cargo")}),
        ("Multimedia", {"fields": ("imagen", "imagen_preview")}),
        ("Configuración", {"fields": ("orden", "activo")}),
    )

    def imagen_preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" style="max-width: 150px; max-height: 150px; border-radius: 50%; object-fit: cover;">'
        return "-"

    imagen_preview.allow_tags = True
    imagen_preview.short_description = "Vista previa"
