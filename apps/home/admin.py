from django.contrib import admin
from .models import Header

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'subtitulo')
    readonly_fields = ('imagen_preview',)
    
    def imagen_preview(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" style="max-width: 200px; max-height: 200px;">'
        return '-'
    imagen_preview.allow_tags = True
    imagen_preview.short_description = 'Vista previa'
