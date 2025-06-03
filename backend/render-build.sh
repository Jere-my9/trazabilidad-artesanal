#!/usr/bin/env bash
set -o errexit # Salir si un comando falla

echo "--- Instalando dependencias de Python ---"
pip install -r requirements.txt

echo "--- Descargando datos de NLTK ---"
# Descarga los recursos necesarios de NLTK a una ubicación conocida
# NLTK_DATA es una variable de entorno que NLTK busca para sus datos
export NLTK_DATA=/opt/render/project/src/nltk_data
mkdir -p $NLTK_DATA # Asegurarse de que el directorio exista

python -c "import nltk; nltk.download('punkt', download_dir='$NLTK_DATA')"
python -c "import nltk; nltk.download('averaged_perceptron_tagger', download_dir='$NLTK_DATA')"
python -c "import nltk; nltk.download('wordnet', download_dir='$NLTK_DATA')"
python -c "import nltk; nltk.download('punkt_tab', download_dir='$NLTK_DATA')"

echo "--- Ejecutando migraciones de Django ---"
python manage.py migrate

echo "--- Recolectando archivos estáticos de Django (opcional si usas S3/Cloudinary para estáticos) ---"
python manage.py collectstatic --noinput

echo "--- Proceso de construcción de Render completado ---"