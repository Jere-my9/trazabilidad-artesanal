import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import os
import requests # <--- AÑADIR ESTA LÍNEA
from PIL import Image # <--- AÑADIR ESTA LÍNEA
import io # <--- AÑADIR ESTA LÍNEA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_WEIGHTS_PATH = os.path.join(BASE_DIR, 'mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224.h5')
model = None

try:
    print(f"DEBUG: Intentando cargar MobileNetV2 desde: {MODEL_WEIGHTS_PATH}")
    model = MobileNetV2(weights=None, include_top=True, input_shape=(224, 224, 3))
    model.load_weights(MODEL_WEIGHTS_PATH)
    print("DEBUG: Modelo MobileNetV2 cargado con éxito desde el archivo local.")
except Exception as e:
    print(f"ERROR: Fallo al cargar MobileNetV2 desde {MODEL_WEIGHTS_PATH}: {e}")
    model = None

TERMINOS_AUTENTICIDAD = [
    'woven', 'handicraft', 'scarf', 'basket', 'hat', 'bag',
    'carpet', 'tapestry', 'pottery', 'necklace', 'bracelet',
    'wool', 'embroidery', 'fabric', 'shawl', 'pouch'
]

# Modificar la función verificar_producto
def verificar_producto(imagen_url): # Cambiamos el nombre del parámetro a imagen_url para claridad
    if model is None:
        print("ERROR: Intento de verificar producto sin que el modelo de IA esté cargado.")
        return False, 0.0, "Error interno del servidor: El modelo de IA no está disponible."

    try:
        # === CAMBIOS A REALIZAR AQUÍ ===
        # Descargar la imagen desde la URL
        response = requests.get(imagen_url)
        response.raise_for_status() # Lanza un error para códigos de estado HTTP 4xx/5xx

        # Leer la imagen directamente desde la respuesta
        img = Image.open(io.BytesIO(response.content))
        img = img.resize((224, 224)) # Redimensionar la imagen (target_size)

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        decoded = decode_predictions(preds, top=5)[0]

        confianza_max = 0.0
        es_autentico = False

        for _, label, score in decoded:
            if score > confianza_max:
                confianza_max = score

            if any(term in label.lower() for term in TERMINOS_AUTENTICIDAD):
                es_autentico = True

        return es_autentico, round(confianza_max * 100, 2), "Verificación exitosa"

    except requests.exceptions.RequestException as e:
        print(f"ERROR: Fallo al descargar la imagen desde la URL {imagen_url}: {e}")
        return False, 0.0, f"Error al acceder a la imagen para verificación: {e}"
    except Exception as e:
        print(f"ERROR en verificar_producto: {e}")
        return False, 0.0, f"Error durante la verificación de la imagen: {e}"