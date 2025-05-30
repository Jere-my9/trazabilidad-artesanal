from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoArtesanalViewSet

router = DefaultRouter()
router.register(r'productos', ProductoArtesanalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
