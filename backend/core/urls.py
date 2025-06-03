# backend/core/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

# === INICIO DE CAMBIOS ===

# Esta línea solo debe estar activa en MODO DEBUG (desarrollo local).
# En producción, Cloudinary manejará los archivos de medios.
if settings.DEBUG: # <--- AÑADIR ESTA LÍNEA
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# === FIN DE CAMBIOS ===