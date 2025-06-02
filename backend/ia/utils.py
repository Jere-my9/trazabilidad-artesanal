import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import os

# Determina la ruta base de tu aplicación (la carpeta 'IA')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define la ruta completa al archivo de pesos del modelo dentro de tu proyecto
# Asegúrate de que 'mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224.h5'
# sea el nombre EXACTO del archivo que copiaste.
MODEL_WEIGHTS_PATH = os.path.join(BASE_DIR, 'mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224.h5')

# Variable global para el modelo (inicialmente None)
model = None

# Cargar el modelo MobileNetV2 con los pesos locales al iniciar la aplicación
try:
    print(f"DEBUG: Intentando cargar MobileNetV2 desde: {MODEL_WEIGHTS_PATH}")
    # Crea una instancia del modelo MobileNetV2 sin pesos iniciales
    # Es crucial que weights=None aquí para evitar que Keras intente descargarlos.
    model = MobileNetV2(weights=None, include_top=True, input_shape=(224, 224, 3))
    # Carga los pesos desde tu archivo local
    model.load_weights(MODEL_WEIGHTS_PATH)
    print("DEBUG: Modelo MobileNetV2 cargado con éxito desde el archivo local.")
except Exception as e:
    # Si la carga falla, imprime el error y asegura que 'model' sea None
    print(f"ERROR: Fallo al cargar MobileNetV2 desde {MODEL_WEIGHTS_PATH}: {e}")
    # Para depuración, podríamos levantar el error temporalmente:
    # raise e
    model = None

TERMINOS_AUTENTICIDAD = [
    'woven', 'handicraft', 'scarf', 'basket', 'hat', 'bag',
    'carpet', 'tapestry', 'pottery', 'necklace', 'bracelet',
    'wool', 'embroidery', 'fabric', 'shawl', 'pouch'
]

def verificar_producto(imagen_path):
    if model is None:
        print("ERROR: Intento de verificar producto sin que el modelo de IA esté cargado.")
        return False, "Error interno del servidor: El modelo de IA no está disponible."

    try:
        img = image.load_img(imagen_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        decoded = decode_predictions(preds, top=5)[0]

        for _, label, _ in decoded:
            if any(term in label.lower() for term in TERMINOS_AUTENTICIDAD):
                return True, label

        return False, decoded[0][1]
    except Exception as e:
        return False, f"Error durante la verificación de la imagen: {e}"