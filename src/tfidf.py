def calc_TF_IDF(matriz_terminos):
    for i in range(len(matriz_terminos)):
        for j in range(len(matriz_terminos[i])):
            matriz_terminos[i][j][2] =  matriz_terminos[i][j][0] *  matriz_terminos[i][j][1]
