# C:\Tinkuy-trazabilidad\backend\api\serializers.py

from rest_framework import serializers
from .models import ProductoArtesanal, TipoProducto # Asegúrate de importar TipoProducto

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__' # O especifica los campos que quieres serializar, ej. ['id', 'nombre']

class ProductoArtesanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoArtesanal
        fields = '__all__'
        # Asegúrate de que 'tipo' se maneje correctamente si es un ForeignKey o CharField
        # Si 'tipo' es un ForeignKey a TipoProducto, es posible que quieras un Nested Serializer o PrimaryKeyRelatedField
        # Por ahora, con CharField, __all__ funciona.