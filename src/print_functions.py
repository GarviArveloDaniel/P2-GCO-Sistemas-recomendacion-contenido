def print_doc_data(matriz_terminos, terminos, terminos_unicos):
    for doc in range(len(matriz_terminos)):
        print("\n# Documento " + str(doc) + "\n")
        print("Terminos analizados del documento >> " + str(len(terminos[doc])) + " palabras")
        #print(terminos[doc])
        print
        counter = 0 #Numero de palabra
        cabecera = '{:<3} {:<20} {:<3} {:<6} {:<6}'.format("N.", "Termino", "TF", "IDF", "TF-IDF")
        print(cabecera)
        for term in range(len(matriz_terminos[doc])):
            linea_output = []
            if (matriz_terminos[doc][term][0] != 0):
                counter += 1
                linea_output.append(str(counter))
                linea_output.append(str(terminos_unicos[term]))
                linea_output.append(matriz_terminos[doc][term][0])
                #Formatear IDF
                idf_str = "{:.3f}".format(matriz_terminos[doc][term][1])
                linea_output.append(idf_str)
                #Formatear TF-IDF
                tfidf_str = "{:.3f}".format(matriz_terminos[doc][term][2])
                linea_output.append(tfidf_str)

                linea_aux = '{:<3} {:<20} {:<3} {:<6} {:<6}'.format(linea_output[0], linea_output[1], linea_output[2], linea_output[3], linea_output[4])
                print(linea_aux)
        print("---------------------------------------------------------------")


def print_matriz_sim(matrix):
    print("\nSIMILITUD ENTRE DOCUMENTOS\n")
    cabecera = '{:<11}'.format(" ")
    for i in range(len(matrix)):
        index = "[D." + str(i) + "]"
        aux = '{:<9}'.format(index)
        cabecera += aux
    print(cabecera)
    for i in range(len(matrix)):
        output = ""
        aux_fila = "[Doc " + str(i) + "] ->"
        aux = '{:<11}'.format(aux_fila)
        output += aux
        for j in range(len(matrix[i])):
            aux_numero = "{:.3f}".format(matrix[i][j])
            aux_num = '{:<9}'.format(aux_numero)
            output += aux_num
        print (output)