# C:\Tinkuy-trazabilidad\backend\api\models.py

from django.db import models

# Añade esta clase:
class TipoProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True) # Un tipo de producto debe tener un nombre y ser único

    def __str__(self):
        return self.nombre

class ProductoArtesanal(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='productos/')
    creado_en = models.DateTimeField(auto_now_add=True)
    verificado = models.BooleanField(default=False)
    confianza_ia = models.FloatField(default=0.0)
    impacto_social = models.TextField(blank=True)
    hash_blockchain = models.CharField(max_length=256, blank=True)
    # Si 'tipo' de ProductoArtesanal se relaciona con TipoProducto, debería ser un ForeignKey:
    # tipo = models.ForeignKey(TipoProducto, on_delete=models.SET_NULL, null=True, blank=True)
    # Por ahora, para resolver el error, lo dejamos como CharField si no lo vas a relacionar directamente aún
    tipo = models.CharField(max_length=50, blank=True, null=True)


    def __str__(self):
        return self.nombre