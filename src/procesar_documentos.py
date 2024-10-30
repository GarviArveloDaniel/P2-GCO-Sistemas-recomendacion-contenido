import json
import re
from collections import Counter

def procesar_fichero(fichero_principal, fichero_eliminar, fichero_lemas):
    # Leer el fichero principal y almacenar las palabras en una lista junto con sus índices originales
    with open(fichero_principal, 'r', encoding='utf-8') as f:
        texto = f.read()
        texto = re.sub(r"[^\w\s']", ' ', texto)
        palabras = texto.split()

    palabras_con_indices = [(indice, palabra) for indice, palabra in enumerate(palabras)]
    
    # Leer el fichero de palabras a eliminar y almacenarlas en un conjunto
    with open(fichero_eliminar, 'r', encoding='utf-8') as f:
        palabras_a_eliminar = set(f.read().split())
    
    # Filtrar la lista de palabras con índices para eliminar las que están en el conjunto de palabras a eliminar
    palabras_filtradas = [(indice, palabra) for indice, palabra in palabras_con_indices if palabra not in palabras_a_eliminar]
    
    # Leer el fichero de lematización en formato JSON y cargarlo como diccionario
    with open(fichero_lemas, 'r', encoding='utf-8') as f:
        lemas = json.load(f)
    
    # Reemplazar las palabras filtradas con su lema si existe en el diccionario
    palabras_lemmatizadas = [(indice, lemas.get(palabra, palabra)) for indice, palabra in palabras_filtradas]
    
    # Contar las ocurrencias de cada palabra lematizada
    frecuencia_palabras = Counter([palabra for _, palabra in palabras_lemmatizadas])
    
    # Crear el resultado final sin duplicados y con frecuencia de aparición
    resultado = []
    palabras_vistas = set()
    for indice, palabra in palabras_lemmatizadas:
        if palabra not in palabras_vistas:
            resultado.append((indice, palabra, frecuencia_palabras[palabra]))
            palabras_vistas.add(palabra)
    
    return resultado
