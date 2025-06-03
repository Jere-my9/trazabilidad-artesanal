# backend/core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# --- ¡CAMBIO CLAVE AQUÍ! ---
# Esto hará que Django sirva tus archivos de medios incluso en producción.
# ADVERTENCIA: Esta NO es una práctica recomendada para producción real
# porque Django no está optimizado para servir archivos estáticos/media de manera eficiente/segura.
# Pero, hará que funcione como pides, aunque los archivos se perderán con cada reinicio de Render.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
