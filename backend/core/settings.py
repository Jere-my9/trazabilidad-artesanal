import os
import dj_database_url
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production production!
SECRET_KEY = config('SECRET_KEY', default='django-insecure-gz$d%h-1az^d)b-e^tjf*yy&%+w%oh57)z-y&)6p^dck(0-o1)')


# === CONFIGURACIONES PARA PRODUCCIÓN (RENDER) ===
# 1. DEBUG (usar decouple para que sea True en .env y False en Render por defecto)
DEBUG = config('DEBUG', default=False, cast=bool)

# 2. ALLOWED_HOSTS (crucial para Render)
ALLOWED_HOSTS = ['tinkuy-backend.onrender.com'] # Siempre incluye tu dominio de Render
# Añade el hostname externo de Render si está disponible
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Si DEBUG es True (solo en desarrollo local), permite localhost y 127.0.0.1
if DEBUG:
    ALLOWED_HOSTS.extend(['localhost', '127.0.0.1'])


# === INICIO DE CAMBIOS ===

# Configuración de Cloudinary (DESCOMENTAR ESTAS LÍNEAS)
CLOUDINARY_CLOUD_NAME = config('CLOUDINARY_CLOUD_NAME')
CLOUDINARY_API_KEY = config('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = config('CLOUDINARY_API_SECRET')

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
# MEDIA_URL = '/media/' # Cloudinary lo maneja, pero esta línea a veces es necesaria para Django


# Configuración de CORS (¡CRÍTICO para la comunicación frontend/backend!)
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = [
        "https://tinkuy-frontend.onrender.com", # ¡Asegúrate de que esta URL sea EXACTA!
    ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',          # <--- DESCOMENTAR ESTA LÍNEA
    'cloudinary_storage',  # <--- DESCOMENTAR ESTA LÍNEA
    'corsheaders',
    'rest_framework',
    'api',
    'ia',
    'blockchain',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware', # <--- COMENTAR ESTA LÍNEA
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ['DATABASE_URL'],
            conn_max_age=600
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# --- Configuración para Whitenoise y Media Files (COMENTAR ESTAS LÍNEAS) ---
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media' # Asegúrate de que esta línea esté activa y así

# COMENTAR ESTA LÍNEA:
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'