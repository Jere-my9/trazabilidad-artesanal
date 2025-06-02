import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import os

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

def verificar_producto(imagen_path):
    if model is None:
        print("ERROR: Intento de verificar producto sin que el modelo de IA esté cargado.")
        return False, 0.0, "Error interno del servidor: El modelo de IA no está disponible." 

    try:
        img = image.load_img(imagen_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        decoded = decode_predictions(preds, top=5)[0]

        confianza_max = 0.0
        es_autentico = False

        for _, label, score in decoded: # Ahora capturamos el score
            if score > confianza_max:
                confianza_max = score 

            if any(term in label.lower() for term in TERMINOS_AUTENTICIDAD):
                es_autentico = True 

        return es_autentico, round(confianza_max * 100, 2), "Verificación exitosa" 

    except Exception as e:
        print(f"ERROR en verificar_producto: {e}")
        return False, 0.0, f"Error durante la verificación de la imagen: {e}"