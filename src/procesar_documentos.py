import json
import re
from collections import Counter

def procesar_fichero(fichero_principal, fichero_eliminar, fichero_lemas):
    # Leer el fichero de palabras a eliminar y almacenarlas en un conjunto
    with open(fichero_eliminar, 'r', encoding='utf-8') as f:
        palabras_a_eliminar = set(f.read().split())
    
    # Leer el fichero de lematización en formato JSON y cargarlo como diccionario
    with open(fichero_lemas, 'r', encoding='utf-8') as f:
        lemas = json.load(f)
    
    # Leer cada línea del fichero principal como un documento separado
    lista_documentos = []
    with open(fichero_principal, 'r', encoding='utf-8') as f:
        for linea in f:
            # Limpiar y dividir cada línea en palabras
            texto = re.sub(r"[^\w\s']", ' ', linea)  # Eliminar signos de puntuación excepto apóstrofe
            palabras = texto.split()
            
            # Obtener índices originales de palabras en el documento actual
            palabras_con_indices = [(indice, palabra) for indice, palabra in enumerate(palabras)]
            
            # Filtrar palabras que están en el conjunto de palabras a eliminar
            palabras_filtradas = [(indice, palabra) for indice, palabra in palabras_con_indices if palabra not in palabras_a_eliminar]
            
            # Reemplazar las palabras filtradas con su lema si existe en el diccionario
            palabras_lemmatizadas = [(indice, lemas.get(palabra, palabra)) for indice, palabra in palabras_filtradas]
            
            # Contar las ocurrencias de cada palabra lematizada en el documento
            frecuencia_palabras = Counter([palabra for _, palabra in palabras_lemmatizadas])
            
            # Crear lista de términos únicos con sus frecuencias
            resultado_documento = []
            palabras_vistas = set()
            for indice, palabra in palabras_lemmatizadas:
                if palabra not in palabras_vistas:
                    resultado_documento.append((indice, palabra, frecuencia_palabras[palabra]))
                    palabras_vistas.add(palabra)
            
            # Agregar resultado del documento a la lista de documentos
            lista_documentos.append(resultado_documento)
    
    return lista_documentos
