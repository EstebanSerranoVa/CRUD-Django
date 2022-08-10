from django.db import models

# Create your models here.
class Valija(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100, verbose_name='Nombre')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name='Imagen', null=True)
    descripcion = models.TextField(verbose_name='Descripción',null=True)
    
    def __str__(self):
        fila = "Nombre: " + self.Nombre + " - " + "Descripción: " + self.descripcion
        return fila
    
    def delete(self,using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()