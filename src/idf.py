import math
from collections import defaultdict

def idf(lista_documentos):
    """
    Calcula el IDF (Inverse Document Frequency) para cada término en una lista de documentos.

    Args:
        lista_documentos (list): Lista de documentos, donde cada documento es una lista de tuplas
                                 (índice, término, frecuencia) para cada término único.

    Returns:
        dict: Diccionario con términos como claves y su valor de IDF como valor.
    """
    # Total de documentos
    num_documentos = len(lista_documentos)
    
    # Contar en cuántos documentos aparece cada término
    doc_frecuencia = defaultdict(int)
    for documento in lista_documentos:
        # Utilizar un conjunto para asegurarnos de contar cada término solo una vez por documento
        terminos_vistos = set()
        for _, termino, _ in documento:
            if termino not in terminos_vistos:
                doc_frecuencia[termino] += 1
                terminos_vistos.add(termino)
    
    # Calcular el IDF para cada término
    idf_valores = {}
    for termino, freq in doc_frecuencia.items():
        idf_valores[termino] = math.log(num_documentos / (freq), 10)  # Usar logaritmo para evitar división por cero
    
    return idf_valores