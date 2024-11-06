import math
from collections import defaultdict

def calcular_tf_idf(lista_documentos, idf_values):
    """
    Calcula el TF-IDF para cada término en cada documento utilizando frecuencia relativa.

    Args:
        lista_documentos (list): Lista de documentos, donde cada documento es una lista de tuplas
                                 (índice, término, frecuencia) para cada término único.
        idf_values (dict): Diccionario con IDF de cada término.
    
    Returns:
        list: Lista de diccionarios con TF-IDF por documento.
    """
    tf_idf_docs = []

    for documento in lista_documentos:
        # Calcular el total de términos en el documento
        total_terminos = sum(freq for _, _, freq in documento)
        
        # Calcular TF-IDF para cada término en el documento
        tf_idf_doc = {}
        for _, termino, freq in documento:
            tf = freq / total_terminos  # Frecuencia relativa
            tf_idf_doc[termino] = tf * idf_values.get(termino, 0)  # TF-IDF
        tf_idf_docs.append(tf_idf_doc)

    return tf_idf_docs