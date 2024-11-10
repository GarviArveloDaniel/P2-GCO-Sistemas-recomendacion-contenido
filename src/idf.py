import math

def calc_IDF(matriz_terminos):
    """
    Calcula el valor de IDF (Inverse Document Frequency) para cada término en un conjunto de documentos.

    Este método calcula el IDF de cada término en una matriz de términos. El IDF mide la importancia
    de un término en el conjunto de documentos, siendo más alto cuando el término aparece en menos documentos.

    La fórmula de IDF es:
        IDF(t) = log(N / df(t)), donde:
            - N: el número total de documentos.
            - df(t): el número de documentos en los que aparece el término t.

    El valor de IDF es almacenado en la matriz de términos en la posición correspondiente al término
    y documento en cuestión.
    """
    N = len(matriz_terminos)
    for i in range(len(matriz_terminos)):
        for j in range(len(matriz_terminos[i])):
            docs_aparece = 0
            # Buscar si la palabra aparece en los documentos
            for cont in range(len(matriz_terminos)):
                if (matriz_terminos[cont][j][0] != 0): # SI TF != 0 significa que al menos ha aparecido una vez
                    docs_aparece += 1 #La palabra aparece en el documento
            valor = math.log((N/ float(docs_aparece)),10)
            matriz_terminos[i][j][1] = valor