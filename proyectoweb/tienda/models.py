from django.db import models

class CategoriaPro(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    categoria=models.ForeignKey(CategoriaPro, on_delete=(models.CASCADE))
    imagen=models.ImageField(upload_to='tienda')
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
        
    def __str__(self):
        return self.nombre
    
