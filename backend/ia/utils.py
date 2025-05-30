import numpy as np
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import os

# Cargar modelo MobileNet preentrenado
model = MobileNetV2(weights='imagenet')

TERMINOS_AUTENTICIDAD = [
    'woven', 'handicraft', 'scarf', 'basket', 'hat', 'bag',
    'carpet', 'tapestry', 'pottery', 'necklace', 'bracelet',
    'wool', 'embroidery', 'fabric', 'shawl', 'pouch'
]

def verificar_producto(imagen_path):
    try:
        img = image.load_img(imagen_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = model.predict(x)
        decoded = decode_predictions(preds, top=5)[0]  # Más resultados

        for _, label, _ in decoded:
            if any(term in label.lower() for term in TERMINOS_AUTENTICIDAD):
                return True, label

        return False, decoded[0][1]
    except Exception as e:
        return False, str(e)
