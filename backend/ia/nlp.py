import random
import nltk

def generar_impacto_social(nombre, descripcion):
    # Tokenizamos y extraemos sustantivos clave
    palabras = nltk.word_tokenize(descripcion)
    etiquetas = nltk.pos_tag(palabras)
    sustantivos = [palabra for palabra, tipo in etiquetas if tipo.startswith("NN")]

    if not sustantivos:
        sustantivos = ["producto artesanal"]

    sustantivo_principal = sustantivos[0]

    plantillas = [
        f"{sustantivo_principal} ha sido elaborado cuidadosamente por comunidades locales, preservando técnicas ancestrales.",
        f"{sustantivo_principal} refleja una historia única de tradición, identidad y sostenibilidad.",
        f"{sustantivo_principal} forma parte de un proyecto que empodera a pequeños productores y promueve el comercio justo.",
        f"Este producto representa el esfuerzo colectivo de artesanos que mantienen viva la herencia cultural de su región.",
    ]

    return random.choice(plantillas)
