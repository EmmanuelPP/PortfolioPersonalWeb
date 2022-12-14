from django.db import models
from django.db.models.fields import URLField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    description = models.CharField(max_length=200, verbose_name = 'Descripcion')
    image = models.ImageField(verbose_name = 'Imagen', upload_to = 'projects')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    link = models.URLField(blank=True, null=True, verbose_name= 'Direccion Web')


    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
    
    def __str__(self):
        return self.title