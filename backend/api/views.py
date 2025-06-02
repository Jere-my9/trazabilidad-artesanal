# backend/tinkuy_backend/api/views.py

import os
from rest_framework import viewsets
from .models import ProductoArtesanal
from .serializers import ProductoArtesanalSerializer
from ia.utils import verificar_producto 
from ia.nlp import generar_impacto_social # Descomenta esta línea
# from blockchain.utils import registrar_en_blockchain 

class ProductoArtesanalViewSet(viewsets.ModelViewSet):
    queryset = ProductoArtesanal.objects.all().order_by('-creado_en')
    serializer_class = ProductoArtesanalSerializer

    def perform_create(self, serializer):
        producto = serializer.save()
        
        if producto.imagen: 
            try:
                verificado, _ = verificar_producto(producto.imagen.path) 
                producto.verificado = verificado
                print(f"DEBUG: Producto verificado por IA: {verificado}")
            except Exception as e:
                print(f"ERROR: Fallo al verificar producto con IA: {e}")
                producto.verificado = False 
        
        # --- Descomenta ESTE bloque para generar impacto social ---
        try:
            impacto = generar_impacto_social(producto.nombre, producto.descripcion) # Descomenta esta sección
            producto.impacto_social = impacto
            print(f"DEBUG: Impacto social generado: {impacto}")
        except Exception as e:
            print(f"ERROR: Fallo al generar impacto social: {e}")
            producto.impacto_social = "" 


        # El bloque de blockchain permanece comentado
        # try:
        #     tx_hash, hash_hex = registrar_en_blockchain(producto)
        #     producto.hash_blockchain = hash_hex
        #     print(f"DEBUG: Hash Blockchain: {hash_hex}")
        # except Exception as e:
        #     print(f"ERROR: Error registrando en blockchain: {e}")
        #     producto.hash_blockchain = "" 

        producto.save()