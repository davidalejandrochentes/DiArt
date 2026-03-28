from django.db import models

class Header(models.Model):
    subtitulo = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='header/')
    
    class Meta:
        verbose_name = 'Header'
        verbose_name_plural = 'Header'
    
    def __str__(self):
        return self.titulo
