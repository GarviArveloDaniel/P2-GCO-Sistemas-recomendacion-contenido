import math
import numpy as np

def calc_sim_cos(doc1, doc2, terminos_unicos, matriz_terminos):
    """
    Calcula la similitud entre dos documentos utilizando el Coseno de los vectores de TF-IDF.

    La similitud entre los documentos se calcula usando la fórmula del coseno del ángulo entre
    dos vectores de términos representados por sus valores TF-IDF.

    Parámetros:
    -----------
    doc1 : int --> El índice del primer documento en la matriz de términos.
    
    doc2 : int --> El índice del segundo documento en la matriz de términos.
    
    terminos_unicos : list --> Lista de todos los términos únicos presentes en el conjunto de documentos.
    
    matriz_terminos : list[list[list]]
        Una matriz tridimensional donde cada fila representa un documento, y cada columna contiene
        los términos en el documento. Cada término tiene tres valores asociados: [TF, IDF, TF-IDF],
        de los cuales solo se usa el valor de TF-IDF para calcular la similitud.

    """
    numerador = 0
    denominador_izq = 0
    denominador_der = 0
    for i in range(len(terminos_unicos)):
       numerador += matriz_terminos[doc1][i][2] * matriz_terminos[doc2][i][2]
       denominador_izq += pow(matriz_terminos[doc1][i][2],2)
       denominador_der += pow(matriz_terminos[doc2][i][2],2)
    denominador = math.sqrt(denominador_der) * math.sqrt(denominador_izq)
    
    # En caso de error (denominador 0) lanzamos un error y terminamos.
    if denominador == 0:
        doc_error = 0
        if denominador_izq == 0:
            doc_error = doc1
        else:
            doc_error = doc2
        out_text = "ERROR: Division por cero -> En el documento " + str(doc_error) + "todos sus terminos tienen TF-IDF = 0. Por tanto todas las palabras aparecen en todos los documentos"
        raise SystemExit(out_text)
    
    return (numerador/float(denominador))