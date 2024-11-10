def calc_TF_IDF(matriz_terminos):
    """
    Calcula el valor de TF-IDF para cada término en cada documento.

    El valor de **TF-IDF (Term Frequency - Inverse Document Frequency)** es una medida que evalúa la importancia
    de una palabra en un documento dentro de un conjunto de documentos. El **TF** mide cuántas veces aparece
    un término en un documento, mientras que el **IDF** mide la importancia de un término en el corpus global.
    El producto de ambos valores da como resultado el **TF-IDF**, que se usa para ponderar la relevancia de los términos.

    Parámetros:
    -----------
    matriz_terminos : list[list[list]]
        Una matriz tridimensional donde cada fila representa un documento y cada columna contiene un término. 
        Cada término tiene tres valores asociados: 
        - `matriz_terminos[i][j][0]`: TF (frecuencia del término en el documento).
        - `matriz_terminos[i][j][1]`: IDF (frecuencia inversa del término en el corpus).
        - `matriz_terminos[i][j][2]`: TF-IDF (que será calculado en esta función).

    Retorna:
    --------
        La función no retorna ningún valor, pero modifica la matriz_terminos directamente,
        actualizando la columna de TF-IDF para cada término en cada documento.
    """
    for i in range(len(matriz_terminos)):
        for j in range(len(matriz_terminos[i])):
            matriz_terminos[i][j][2] =  matriz_terminos[i][j][0] *  matriz_terminos[i][j][1]
