from django.db import models

'''
Title: Un título con 200 caracteres de longitud máxima.
Subtitle: Un subtítulo con 200 caracteres de longitud máxima.
Content: Un texto de tamaño indefinido.
Image: Una imagen para mostrar de fondo almacenada en el directorio services (dentro de media).
Created: Un campo automático para gestionar la fecha y hora de creación.
Updated: Un campo automático para gestionar la fecha y hora de última actualización.
'''

# Create your models here.

class service(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo")
    subtitle = models.CharField(max_length=200, verbose_name = "Subtitulo")
    content = models.TextField(verbose_name = "Contenido")
    image = models.ImageField(verbose_name = "Imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edición")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]

    def __str__(self):
        return self.title
