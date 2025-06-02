#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -m nltk.downloader punkt
python -m nltk.downloader averaged_perceptron_tagger
python -m nltk.downloader wordnet
# Descargar el recurso específico que falta
python -c "import nltk; nltk.download('punkt_tab', download_dir='/opt/render/project/src/nltk_data')"
# Puedes añadir más si tu código usa otros recursos de NLTK (ej. 'stopwords', 'vader_lexicon', etc.)

# Run migrations
python manage.py migrate