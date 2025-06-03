# backend/tinkuy_backend/api/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ProductoArtesanal, TipoProducto
from .serializers import ProductoArtesanalSerializer, TipoProductoSerializer
from ia.utils import verificar_producto # Asegúrate de que esta importación exista
# from blockchain.utils import registrar_en_blockchain # <-- Comenta o elimina esta línea
import logging

logger = logging.getLogger(__name__)

class ProductoArtesanalViewSet(viewsets.ModelViewSet):
    queryset = ProductoArtesanal.objects.all()
    serializer_class = ProductoArtesanalSerializer

    def perform_create(self, serializer):
        logger.debug("Starting create process for ProductoArtesanal")
        producto = serializer.save()

        # 1. Verificar el producto con IA
        try:
            # Asegúrate de que 'image' es el campo correcto de tu modelo
            if producto.imagen and hasattr(producto.imagen, 'path'):
                # Si ya está guardada en Cloudinary, 'path' puede no existir
                # Necesitarás pasar la URL de Cloudinary a la función de IA
                imagen_path_o_url = producto.imagen.url # Usar la URL de Cloudinary
            else:
                # Si no hay imagen o no tiene URL, o para pruebas locales
                logger.warning("Producto sin imagen o URL de imagen no disponible para IA.")
                imagen_path_o_url = None

            confianza_ia, _ = verificar_producto(imagen_path_o_url) # Pasar la URL
            producto.confianza_ia = confianza_ia
            producto.verificado = confianza_ia >= 70.0 # Define tu umbral de confianza
            producto.save() # Guardar la confianza y verificación IA

            logger.debug(f"DEBUG: Producto verificado por IA: {producto.verificado}, Confianza: {producto.confianza_ia}%")

        except Exception as e:
            logger.error(f"ERROR: Fallo al verificar con IA: {e}")
            producto.confianza_ia = 0.0
            producto.verificado = False
            producto.save()


        # 2. Registrar en blockchain (DESACTIVADO TEMPORALMENTE)
        try:
            # Si tienes una línea como esta, coméntala o bórrala:
            # tx_hash, hash_prod = registrar_en_blockchain(producto)
            # producto.hash_blockchain = tx_hash
            # producto.save() # Guardar el hash de la blockchain

            logger.warning("Blockchain integration is temporarily disabled.")
            producto.hash_blockchain = "Blockchain Desactivada" # O déjalo vacío
            producto.save() # Guardar el cambio si hiciste uno
        except Exception as e:
            logger.error(f"ERROR: Fallo al registrar en blockchain: {e}")
            producto.hash_blockchain = "ERROR: Fallo al registrar"
            producto.save() # Guardar el error


class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer