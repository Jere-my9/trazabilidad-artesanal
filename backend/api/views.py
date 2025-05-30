import os
from rest_framework import viewsets
from .models import ProductoArtesanal
from .serializers import ProductoArtesanalSerializer
from ia.utils import verificar_producto
from ia.nlp import generar_impacto_social
from blockchain.utils import registrar_en_blockchain

class ProductoArtesanalViewSet(viewsets.ModelViewSet):
    queryset = ProductoArtesanal.objects.all().order_by('-creado_en')
    serializer_class = ProductoArtesanalSerializer

    def perform_create(self, serializer):
        producto = serializer.save()
        imagen_path = producto.imagen.path

        verificado, _ = verificar_producto(imagen_path)
        producto.verificado = verificado

        impacto = generar_impacto_social(producto.nombre, producto.descripcion)
        producto.impacto_social = impacto

        try:
            tx_hash, hash_hex = registrar_en_blockchain(producto)
            producto.hash_blockchain = hash_hex  # agrega este campo al modelo si aún no lo tienes
        except Exception as e:
            print("Error registrando en blockchain:", e)

        producto.save()

