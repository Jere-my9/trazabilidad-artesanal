from rest_framework import serializers
from .models import ProductoArtesanal

class ProductoArtesanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoArtesanal
        fields = '__all__'
