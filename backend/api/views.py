import os
from rest_framework import viewsets
from .models import ProductoArtesanal
from .serializers import ProductoArtesanalSerializer
# from ia.utils import verificar_producto # Comenta esta línea
# from ia.nlp import generar_impacto_social # Comenta esta línea
# from blockchain.utils import registrar_en_blockchain # Comenta esta línea

class ProductoArtesanalViewSet(viewsets.ModelViewSet):
    queryset = ProductoArtesanal.objects.all().order_by('-creado_en')
    serializer_class = ProductoArtesanalSerializer

    def perform_create(self, serializer):
        # Primero, guarda el producto para que la imagen se suba y el path esté disponible
        producto = serializer.save()
        
        # Opcional: Puedes imprimir la ruta de la imagen para verificarla si no se comenta todo lo de IA/Blockchain
        # print(f"DEBUG: Imagen guardada en: {producto.imagen.path}")

        # --- Comenta todas las llamadas a IA y Blockchain por ahora ---
        # if producto.imagen: # Asegúrate de que hay una imagen antes de intentar verificar
        #     try:
        #         verificado, _ = verificar_producto(producto.imagen.path)
        #         producto.verificado = verificado
        #         print(f"DEBUG: Producto verificado por IA: {verificado}")
        #     except Exception as e:
        #         print(f"ERROR: Fallo al verificar producto con IA: {e}")
        #         producto.verificado = False # Asegúrate de un valor por defecto si falla
        
        # try:
        #     impacto = generar_impacto_social(producto.nombre, producto.descripcion)
        #     producto.impacto_social = impacto
        #     print(f"DEBUG: Impacto social generado: {impacto}")
        # except Exception as e:
        #     print(f"ERROR: Fallo al generar impacto social: {e}")
        #     producto.impacto_social = "" # Asegúrate de un valor por defecto si falla


        # try:
        #     tx_hash, hash_hex = registrar_en_blockchain(producto)
        #     producto.hash_blockchain = hash_hex
        #     print(f"DEBUG: Hash Blockchain: {hash_hex}")
        # except Exception as e:
        #     print(f"ERROR: Error registrando en blockchain: {e}")
        #     producto.hash_blockchain = "" # Asegúrate de un valor por defecto si falla
        # --- Fin de las llamadas comentadas ---

        producto.save() # Guarda los cambios (verificado, impacto_social, hash_blockchain si se hubieran modificado)
