import json

def procesar_fichero(fichero_principal, fichero_eliminar, fichero_lemas):
    # Leer el fichero principal y almacenar las palabras en una lista
    with open(fichero_principal, 'r', encoding='utf-8') as f:
        palabras = f.read().split()
    
    # Leer el fichero de palabras a eliminar y almacenarlas en un conjunto
    with open(fichero_eliminar, 'r', encoding='utf-8') as f:
        palabras_a_eliminar = set(f.read().split())
    
    # Filtrar la lista de palabras para eliminar las que están en el conjunto de palabras a eliminar
    palabras_filtradas = [palabra for palabra in palabras if palabra not in palabras_a_eliminar]
    
    # Leer el fichero de lematización en formato JSON y cargarlo como diccionario
    with open(fichero_lemas, 'r', encoding='utf-8') as f:
        lemas = json.load(f)
    
    # Reemplazar las palabras filtradas con su lema si existe en el diccionario
    palabras_finales = [lemas.get(palabra, palabra) for palabra in palabras_filtradas]
    
    return palabras_finales

# Ejemplo de uso:
resultado = procesar_fichero('documents-01.txt', 'stop-words-en.txt', 'corpus-en.txt')
print(resultado)
