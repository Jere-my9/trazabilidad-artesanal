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
            if producto.imagen: # Asegúrate de que haya una imagen
                # --- CAMBIO CLAVE AQUÍ ---
                # Cuando se usa Cloudinary, se pasa la URL de la imagen.
                imagen_path_o_url = producto.imagen.url # <--- CAMBIAR A .url
                logger.debug(f"DEBUG: URL de la imagen para IA: {imagen_path_o_url}") # Cambia el log para reflejar URL
            else:
                logger.warning("Producto sin imagen para IA.")
                imagen_path_o_url = None

            if imagen_path_o_url: # Solo si hay una imagen válida para procesar
                # La función verificar_producto devuelve 3 valores, asegúrate de capturarlos todos
                es_autentico, confianza_ia, mensaje_ia = verificar_producto(imagen_path_o_url)
                producto.confianza_ia = confianza_ia
                producto.verificado = es_autentico # Usar es_autentico directamente o si confianza_ia >= 70.0
                producto.save()

                logger.debug(f"DEBUG: Producto verificado por IA: {producto.verificado}, Confianza: {producto.confianza_ia}%, Mensaje IA: {mensaje_ia}")

            else:
                logger.warning("No se pudo verificar el producto con IA debido a la falta de imagen.")
                producto.confianza_ia = 0.0
                producto.verificado = False
                producto.save() # Guardar el estado sin verificación


        except Exception as e:
            logger.error(f"ERROR: Fallo al verificar con IA: {e}")
            producto.confianza_ia = 0.0
            producto.verificado = False
            producto.save()


        # 2. Registrar en blockchain (DESACTIVADO TEMPORALMENTE)
        try:
            logger.warning("Blockchain integration is temporarily disabled.")
            producto.hash_blockchain = "Blockchain Desactivada" # O déjalo vacío
            producto.save()
        except Exception as e:
            logger.error(f"ERROR: Fallo al registrar en blockchain: {e}")
            producto.hash_blockchain = "ERROR: Fallo al registrar"
            producto.save()


class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer