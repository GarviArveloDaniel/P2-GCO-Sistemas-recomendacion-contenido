from cosine import coseno_similitud
from euclidea import similitud_euclidea
from pearson import pearson
import argparse
from colorama import Fore, Style, init
from procesar_documentos import procesar_fichero
import pandas as pd


# Inicializar colorama
init()


def main():
    # Cargar los documentos y procesar términos y frecuencias
    resultado, idf_valores = procesar_fichero(
        '../data/documents/documents-01.txt', 
        '../data/stop-words/stop-words-en.txt', 
        '../data/corpus/corpus-en.txt'
    )
    
    # Crear la tabla con las columnas y añadir la columna de TF-IDF
    filas = []
    for documento in resultado:
        filas_documento = [
            (
                indice,  # Índice del término
                termino,  # Término
                tf_val,  # TF
                idf_valores.get(termino, 0),  # IDF
                tf_val * idf_valores.get(termino, 0)  # TF-IDF
            )
            for indice, termino, tf_val in documento
        ]
        filas.extend(filas_documento)
        
    # Crear DataFrame con columnas `Índice del término`, `Término`, `TF`, `IDF` y `TF-IDF`
    tabla_resultado = pd.DataFrame(filas, columns=["Índice del término", "Término", "TF", "IDF", "TF-IDF"])
    
    # Aplicar colores a las cabeceras
    print(
        Fore.GREEN + "Índice del término".ljust(20) + Style.RESET_ALL +
        Fore.BLUE + "Término".ljust(15) + Style.RESET_ALL +
        Fore.YELLOW + "TF".ljust(8) + Style.RESET_ALL +
        Fore.CYAN + "IDF".ljust(10) + Style.RESET_ALL +
        Fore.MAGENTA + "TF-IDF".ljust(10) + Style.RESET_ALL
    )
    
    # Imprimir cada fila con ancho de columna ajustado
    for _, row in tabla_resultado.iterrows():
        print(
            Fore.GREEN + f"{int(row['Índice del término']):<20}" + Style.RESET_ALL +
            Fore.BLUE + f"{row['Término']:<15}" + Style.RESET_ALL +
            Fore.YELLOW + f"{row['TF']:<8}" + Style.RESET_ALL +
            Fore.CYAN + f"{row['IDF']:<10.5f}" + Style.RESET_ALL +
            Fore.MAGENTA + f"{row['TF-IDF']:<10.5f}" + Style.RESET_ALL
        )

if __name__ == "__main__":
    main()