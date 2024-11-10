import argparse
import sys
import json
from cosine import calc_sim_cos
from tfidf import calc_TF_IDF
from idf import calc_IDF
from print_functions import print_doc_data, print_matriz_sim


# Contar cantidad de veces que aparecen las palabras
def CountFrequency(my_list):
    count = {}
    for i in my_list:
        count[i] = count.get(i, 0) + 1
    return count

# Rellenar la matriz con TF
def calc_TF(terminos, matriz_terminos, terminos_unicos):
    for doc in range(len(terminos)):
        recuento = CountFrequency(terminos[doc])
        for k,v in recuento.items():
            matriz_terminos[doc][terminos_unicos.index(k)][0] = v

# Rellenar la matriz de similitud entre documentos
def fill_matriz_sim(matriz_sim, terminos_unicos, matriz_terminos):
    for i in range(len(matriz_sim)):
        for j in range(len(matriz_sim[i])):
            matriz_sim[i][j] = calc_sim_cos(i, j, terminos_unicos, matriz_terminos)


def main():
    parser = argparse.ArgumentParser(description='Sistema de recomendación basado en el contenido')
    parser.add_argument('-f', '--file', type=argparse.FileType('r'), required=True, help='Ruta del fichero de entrada')
    parser.add_argument('-o', '--outfile', type=argparse.FileType('w'), required=False, help='Ruta del fichero para almacenar la salida')
    args = parser.parse_args()

    original_stdout = sys.stdout

    if args.outfile is None:
        print("RECOMENDADOR BASADO EN EL CONOCIMIENTO - Modo pantalla")
    else:
        sys.stdout = args.outfile
        print ("RECOMENDADOR BASADO EN EL CONOCIMIENTO\n")
        print ("Fichero de entrada: " + str(args.file.name))
        print("Resultado guardado en: " + str(args.outfile.name))

    linea_fichero = args.file.readlines() # Devuelve un vector de strings

    terminos = []
    for i in linea_fichero:
        doc = []
        elemento = i.split()
        for j in elemento:
            j = j.replace(",","")
            j = j.replace(".","")
            j = j.lower()
            doc.append(j)
        terminos.append(doc)

    stop_words = []
    f = open('../data/stop-words/stop-words-en.txt', 'r')
    stop_words = f.read()
    f.close()
    # Sustituir las stopwords por -
    for t in range(len(terminos)):
        for i in range(len(terminos[t])):
            if terminos[t][i] in stop_words:
                terminos[t][i] = "-"

    # Eliminar los elementos marcados por -
    for l in range(len(terminos)):
        terminos[l] = [i for i in terminos[l] if i != "-"]

    # Lematizacion de los términos resultantes
    f = open('../data/corpus/corpus-en.txt', 'r')
    lemas = json.load(f)
    f.close()
    for t in range(len(terminos)):
        for i in range(len(terminos[t])):
            terminos[t][i] = lemas.get(terminos[t][i], terminos[t][i])

    # Eliminar términos repetidos
    terminos_unicos = []
    for doc_list in terminos:
        for elemento in doc_list:
            if elemento not in terminos_unicos:
                terminos_unicos.append(elemento)

    # Matriz de terminos donde se almacenan los valores [TF, IDF, TF-IDF]
    matriz_terminos = [ [ [0,0,0] for y in range(len(terminos_unicos)) ] for x in range( len(terminos)) ] #Primero col, luego filas

    # Matriz de similitud de documentos
    matriz_sim = [ [ 0 for y in range(len(terminos)) ] for x in range(len(terminos)) ] #Primero col, luego filas

    calc_TF(terminos, matriz_terminos, terminos_unicos)
    calc_IDF(matriz_terminos)
    calc_TF_IDF(matriz_terminos)
    fill_matriz_sim(matriz_sim, terminos_unicos, matriz_terminos)
    print_doc_data(matriz_terminos, terminos, terminos_unicos)
    print_matriz_sim(matriz_sim)

    # Cerramos los ficheros abiertos
    args.file.close()
    if args.outfile is not None:
        args.outfile.close()
        sys.stdout = original_stdout


if __name__ == "__main__":
    main()
