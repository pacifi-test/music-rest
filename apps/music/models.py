from django.db import models 


class Autor(models.Model):
    nombre = models.CharField(u'Nombre', max_length=100)
    descripcion = models.TextField(u'Descripción',)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return nombre
