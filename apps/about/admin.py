from django.contrib import admin
from .models import About


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    readonly_fields = ("imagen_1_preview", "imagen_2_preview")

    fieldsets = (
        (
            "Contenido principal",
            {"fields": ("texto_general", "imagen_1", "imagen_1_preview")},
        ),
        (
            "Estadísticas",
            {
                "fields": (
                    "proyectos_completados",
                    "anios_experiencia",
                    "clientes_felices",
                )
            },
        ),
        (
            "Página de detalle",
            {"fields": ("mision", "vision", "imagen_2", "imagen_2_preview")},
        ),
    )

    def imagen_1_preview(self, obj):
        if obj.imagen_1:
            return f'<img src="{obj.imagen_1.url}" style="max-width: 200px; max-height: 200px; border-radius: 8px;">'
        return "-"

    imagen_1_preview.allow_tags = True
    imagen_1_preview.short_description = "Vista previa imagen 1"

    def imagen_2_preview(self, obj):
        if obj.imagen_2:
            return f'<img src="{obj.imagen_2.url}" style="max-width: 200px; max-height: 200px; border-radius: 8px;">'
        return "-"

    imagen_2_preview.allow_tags = True
    imagen_2_preview.short_description = "Vista previa imagen 2"

    def has_add_permission(self, request):
        if About.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
