# P2-GCO-Sistemas-recomendacion-contenido


# Integrantes del equipo
- Guillermo Díaz Bricio

- Daniel Garvi Arvelo

- Alexander Morales Díaz

- Alba Pérez Rodríguez


# Introducción.

En el contexto de la asignatura, los sistemas de recomendación juegan un papel fundamental al facilitar la búsqueda de información relevante para los usuarios, optimizando así la toma de decisiones y la gestión del conocimiento. Dentro de estos sistemas, los modelos basados en el contenido destacan por su capacidad para recomendar ítems basándose en las características intrínsecas de cada uno de ellos, adaptando las recomendaciones según las preferencias individuales del usuario.


El objetivo de esta práctica es desarrollar un sistema de recomendación utilizando un enfoque basado en el contenido. Este sistema analizará documentos, los procesará para eliminar términos irrelevantes y aplicará métodos de representación y similaridad textual, como el TF-IDF y la similaridad coseno, para medir y comparar la relevancia de los términos entre documentos.


---

# Dependencias
Este sistema de recomendación está desarrollado en Python, por lo que se requieren algunos pasos de instalación y configuración. A continuación, se detallan las instrucciones de instalación de Python y las dependencias necesarias en una terminal de Linux.

## Instalación de Python

En la mayoría de las distribuciones de Linux, Python viene preinstalado. Para verificar si ya tienes Python en tu sistema, abre una terminal y ejecuta:

```bash
python3 --version
```
Si ya tienes Python instalado, este comando te mostrará la versión actual. Si Python no está instalado o necesitas una actualización, sigue estos pasos:

1. Actualizar el índice de paquetes.

Esto asegurará que todos los paquetes del sistema estén en su última versión antes de instalar Python.

```bash
sudo apt update
```

2. Instalar python.

Ejecuta el siguiente comando para instalar Python 3:

```bash
sudo apt install python3
```

3. Instalar pip.

pip es el gestor de paquetes para Python, necesario para instalar las bibliotecas requeridas.
```bash
sudo apt install python3-pip
```

Para verificar que tanto python3 como pip están correctamente instalados, ejecuta los siguientes comandos:
```bash
python3 --version
pip3 --version
```

## Configuración del entorno de pyhton.
Para este proyecto, es recomendable configurar un entorno virtual, lo cual permite gestionar las dependencias del proyecto sin interferir con otras aplicaciones.

1. Instalar el módulo venv.

Si el módulo venv no está instalado, instálalo con el siguiente comando:
```bash
sudo apt install python3-venv
```

2. Crear un entorno virtual.

Dentro del directorio del proyecto, ejecuta el siguiente comando para crear un entorno virtual llamado entorno_recomendador:

```bash
python3 -m venv entorno_recomendador
```
3. Activar el entorno virtual.

Una vez creado, activa el entorno virtual con:

```bash
source entorno_recomendador/bin/activate
```

Cuando el entorno esté activo, deberías ver (entorno_recomendador) antes del prompt de la terminal, indicando que estás en el entorno virtual.

Con el entorno virtual activado, instala las bibliotecas necesarias para el sistema de recomendación utilizando pip. En el caso de este proyecto, las bibliotecas a instalar son numpy y colorama:

```bash
pip install numpy
pip install colorama
```

Estas instrucciones permitirán configurar el entorno de Python en Linux e instalar las bibliotecas necesarias para el sistema de recomendación.

--- 

# Explicación del código implementado
El sistema de recomendación consta de varios módulos, cada uno responsable de una métrica de similitud o una funcionalidad particular. A continuación, se detallan los archivos implementados y su funcionalidad:

## cosine.py
El código implementado es el siguiente:
```bash
import math
import numpy as np

def calc_sim_cos(doc1, doc2, terminos_unicos, matriz_terminos):
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
  ```
El objetivo de este código es calcular la **similaridad coseno** entre dos documentos, una métrica utilizada para medir la similitud entre vectores de términos representados en el espacio vectorial de los documentos. En este caso, cada documento se representa mediante sus valores **TF-IDF** para un conjunto de términos únicos. 

La función `calc_sim_cos` toma los siguientes parámetros:

- `doc1`: Índice del primer documento en la matriz de términos.
- `doc2`: Índice del segundo documento en la matriz de términos.
- `terminos_unicos`: Lista de términos únicos en todos los documentos.
- `matriz_terminos`: Matriz donde cada documento contiene sus términos y sus valores de TF-IDF.

### Cálculo de la Similaridad Coseno

La función calcula la similaridad coseno en varias etapas:

1. **Inicialización de Variables**:
   - `numerador`: Acumula el producto punto entre los vectores TF-IDF de `doc1` y `doc2`.
   - `denominador_izq`: Acumula la norma (magnitud) de los valores TF-IDF de `doc1`.
   - `denominador_der`: Acumula la norma de los valores TF-IDF de `doc2`.

2. **Cálculo del Producto Punto y las Normas**:
   - La función recorre cada término en `terminos_unicos`, calculando el producto punto entre `doc1` y `doc2` para el numerador y sumando los cuadrados de los valores TF-IDF de cada término para el denominador izquierdo (`denominador_izq`) y derecho (`denominador_der`).

3. **Cálculo del Denominador**:
   - La magnitud del denominador se calcula como el producto de las raíces cuadradas de las sumas acumuladas de `denominador_izq` y `denominador_der`.

4. **Manejo de la División por Cero**:
   - Si el `denominador` es cero, lo que implica que los valores TF-IDF para todos los términos de al menos uno de los documentos son cero, se produce un error y el programa se detiene. En este caso, se genera un mensaje de error que indica el índice del documento en el que todos los términos tienen valores TF-IDF iguales a cero.

5. **Resultado de Similaridad**:
   - Si el cálculo procede correctamente, la función retorna la similaridad coseno, calculada como el cociente entre `numerador` y `denominador`.

## idf.py
Código implementado:
```bash
import math

def calc_IDF(matriz_terminos):
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
```

El **IDF** (Frecuencia Inversa de Documento) es una medida que ayuda a determinar la relevancia de un término dentro de un conjunto de documentos. Mientras más raro es un término (es decir, aparece en menos documentos), mayor será su valor de IDF, lo que lo hace más relevante para un documento. Esta métrica es parte fundamental del cálculo del **TF-IDF**, que se utiliza para evaluar la importancia de los términos dentro de un corpus de documentos.

El objetivo de la función `calc_IDF` es calcular el valor de IDF para cada término en una matriz de términos, y actualizar la matriz con los valores correspondientes.

### Parámetros de Entrada

La función toma el siguiente parámetro:
- `matriz_terminos`: Una matriz que representa los documentos y sus términos, donde cada entrada tiene la siguiente estructura:
  - El primer valor en cada celda representa la frecuencia del término en un documento (TF).
  - El segundo valor representa el IDF, que será calculado por esta función.
  - El tercer valor es opcional, dependiendo de la implementación.

### Cálculo del IDF

La función sigue los siguientes pasos:

1. **Inicialización**:
   - La variable `N` almacena el número total de documentos en el conjunto.
   
2. **Recorrer Todos los Términos**:
   - La función recorre la matriz de términos, y para cada término (cada columna de la matriz), se cuenta cuántos documentos contienen ese término. Esto se realiza verificando si el valor de frecuencia de término (`TF`) es diferente de cero, lo que indica que el término aparece al menos una vez en el documento.

3. **Cálculo del IDF**:
   - Para cada término, se calcula el valor de IDF usando la fórmula mencionada anteriormente. Este valor se asigna a la matriz en la posición correspondiente al término y al documento.
   
4. **Actualización de la Matriz**:
   - El valor calculado de IDF se almacena en la matriz de términos, en el segundo valor de cada celda correspondiente al término y documento.


## print_functions.py
El código implementado es el siguiente:
```bash
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

```
En el ámbito de los sistemas de recomendación y procesamiento de documentos, es común representar los documentos en forma de matrices que contienen información sobre los términos y su relevancia (por ejemplo, mediante TF, IDF, y TF-IDF). Para facilitar el análisis de estos datos, es necesario imprimir las matrices de una forma organizada y comprensible.

Las funciones `print_doc_data` y `print_matriz_sim` se encargan de imprimir la información relevante de los documentos procesados. La primera imprime la información de cada término en un documento, mostrando los valores de **TF**, **IDF** y **TF-IDF**. La segunda imprime la matriz de **similaridades coseno** entre documentos, representando las similitudes entre cada par de documentos.


### Función `print_doc_data`

La función `print_doc_data` imprime los datos de los términos de cada documento, mostrando la frecuencia de término (TF), el valor inverso de la frecuencia de documento (IDF) y el valor combinado **TF-IDF**.

#### Parámetros de Entrada
- `matriz_terminos`: Una matriz bidimensional que contiene los datos de los documentos y sus términos. En cada celda de la matriz, se guarda una lista con tres valores: 
  - El primer valor es el **TF** (frecuencia de término en el documento).
  - El segundo valor es el **IDF** (frecuencia inversa de documento).
  - El tercer valor es el **TF-IDF**, que es el producto de los dos anteriores.
  
- `terminos`: Una lista de listas, donde cada sublista representa los términos de cada documento.

- `terminos_unicos`: Una lista de términos únicos que han sido extraídos del conjunto de documentos.

#### Proceso de la Función
1. **Recorrido de Documentos**:
   - Para cada documento en la `matriz_terminos`, la función imprime el número de términos analizados y luego imprime una cabecera de columnas para los datos.
   
2. **Impresión de Datos de Términos**:
   - Para cada término de cada documento, si el **TF** es distinto de cero, se imprimen los siguientes datos:
     - **Número de término** (contador).
     - **Término** (de la lista `terminos_unicos`).
     - **TF** (frecuencia de término).
     - **IDF** (frecuencia inversa de documento).
     - **TF-IDF** (producto de TF e IDF).
   
3. **Formato de Salida**:
   - Los datos se imprimen de manera alineada utilizando la función `format()` para mantener un formato tabular y organizado.


### Función `print_matriz_sim`

La función `print_matriz_sim` es responsable de imprimir la matriz de similitudes coseno entre los documentos de manera organizada y comprensible. Cada elemento de la matriz representa la similitud entre dos documentos, y esta función muestra los resultados en formato tabular.

#### Parámetros de Entrada
- `matrix`: Es una matriz bidimensional de similitudes, donde cada elemento `matrix[i][j]` representa el valor de la similitud coseno entre el documento `i` y el documento `j`.

#### Descripción de la Función
1. **Cabecera de la Tabla**:
   - Se imprime una fila de cabecera que contiene los índices de los documentos en las columnas. Cada documento se indica con el formato `D.i`, donde `i` es el índice del documento.

2. **Impresión de la Matriz de Similitudes**:
   - Luego de la cabecera, se imprimen las filas de la matriz. Cada fila representa un documento y las similitudes con los demás documentos. La similitud entre los documentos se muestra en formato numérico con tres decimales.

#### Proceso
1. **Generación de la Cabecera**:
   - Se construye una cadena con los índices de los documentos para que los valores de similitud se alineen correctamente con los documentos correspondientes en las filas y columnas.
   
2. **Impresión de las Similitudes**:
   - Para cada documento, se imprime una línea que contiene su índice seguido de las similitudes con todos los demás documentos. Los valores se formatean a tres decimales para facilitar su lectura.



## recomendador.py
El código implementado es el siguiente:
```bash
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

```
La función `main` es el punto de entrada del sistema de recomendación basado en contenido. Esta función se encarga de gestionar el flujo del programa, desde la lectura de los datos hasta el cálculo de los valores de TF, IDF, TF-IDF y la similitud entre documentos, y la posterior presentación de los resultados.

### Descripción del Flujo de Trabajo

1. **Lectura de Argumentos de Entrada**:
   - Utiliza la librería `argparse` para leer los argumentos proporcionados por el usuario, tales como el fichero de entrada (`-f`), y la ruta para guardar la salida (`-o`). 
   
2. **Procesamiento del Fichero de Entrada**:
   - Lee el fichero de texto proporcionado y convierte cada línea en una lista de términos (palabras).
   - Se eliminan las palabras de parada (stop words) y se realizan las sustituciones necesarias para limpiar el texto.

3. **Lematización**:
   - Lematiza las palabras usando un diccionario proporcionado en un fichero JSON, reemplazando cada término por su forma lematizada.

4. **Cálculo de TF (Frecuencia de Término)**:
   - La función `calc_TF` calcula la frecuencia de aparición de cada término en cada documento.

5. **Cálculo de IDF (Frecuencia Inversa de Documentos)**:
   - La función `calc_IDF` calcula la frecuencia inversa de los documentos en los que aparece un término, usando la fórmula de IDF.

6. **Cálculo de TF-IDF**:
   - Utiliza los valores de TF y IDF para calcular el valor de TF-IDF de cada término en cada documento.

7. **Cálculo de la Similitud entre Documentos**:
   - La función `fill_matriz_sim` calcula la similitud entre cada par de documentos utilizando el índice de similitud coseno.

8. **Salida de Datos**:
   - Se imprime la tabla de resultados, que incluye los términos, sus valores de TF, IDF, TF-IDF, y la similitud entre los documentos.

9. **Manejo de Archivos de Salida**:
   - Si el usuario ha especificado un fichero de salida, los resultados se escriben en él; de lo contrario, se imprimen en la consola.


## tfidf.py
El código implementado es el siguiente:

```bash
def calc_TF_IDF(matriz_terminos):
    for i in range(len(matriz_terminos)):
        for j in range(len(matriz_terminos[i])):
            matriz_terminos[i][j][2] =  matriz_terminos[i][j][0] *  matriz_terminos[i][j][1]

```

La función `calc_TF_IDF` es responsable de calcular el valor de **TF-IDF** para cada término en cada documento. El valor de **TF-IDF** es un indicador de la importancia de un término dentro de un documento en relación con el corpus total de documentos. Este valor se obtiene multiplicando el **TF (frecuencia de término)** de un término en un documento por el **IDF (frecuencia inversa de documento)** de ese término en el corpus.

### Descripción de la Función

#### Parámetro de Entrada

- **`matriz_terminos`**: Una lista de listas que contiene información sobre cada término en cada documento. Cada elemento de `matriz_terminos` tiene tres valores:
  - **TF** (Frecuencia de Término): El número de veces que el término aparece en un documento.
  - **IDF** (Frecuencia Inversa de Documento): Un valor calculado previamente que refleja la importancia del término en el corpus.
  - **TF-IDF**: Este es el valor que se calculará en esta función y que es el producto de **TF** y **IDF**.

#### Flujo de la Función

1. **Iteración sobre los documentos**: La función recorre todos los documentos en `matriz_terminos`.
2. **Iteración sobre los términos de cada documento**: Para cada documento, la función recorre todos los términos y obtiene sus valores de **TF** (columna 0) y **IDF** (columna 1).
3. **Cálculo de TF-IDF**: La función calcula el valor de **TF-IDF** multiplicando el valor de **TF** por el valor de **IDF** y almacena el resultado en la tercera columna de `matriz_terminos`, que es el índice 2.

--- 

# Ejemplos de uso de la aplicación
Este programa puede ejecutarse de la siguiente forma:
```bash
python3 recomendador.py -f ../data/documents/documents-01.txt -o salida.txt
```
El -f es un argumento de línea de comandos que indica que lo que sigue es el archivo de entrada. En este caso, el archivo es documents-01.txt.

El -o es otro argumento de línea de comandos que indica el archivo de salida. En este caso, salida.txt es el archivo donde se guardarán los resultados generados por el programa.

Al ejecutar dicho comando, se nos creará un nuevo fichero salida.txt que contendrá lo siguiente:

```bash
RECOMENDADOR BASADO EN EL CONOCIMIENTO

Fichero de entrada: ../data/documents/documents-01.txt
Resultado guardado en: salida.txt

# Documento 0

Terminos analizados del documento >> 18 palabras
N.  Termino              TF  IDF    TF-IDF
1   aromas               1   0.301  0.301 
2   include              1   1.000  1.000 
3   tropical             1   1.301  1.301 
4   fruitbroom           1   1.301  1.301 
5   brimstone            1   1.301  1.301 
6   dried                2   1.000  2.000 
7   herb                 1   1.000  1.000 
8   palate               1   0.398  0.398 
9   overly               1   1.301  1.301 
10  expressive           1   1.301  1.301 
11  offer                1   0.699  0.699 
12  unripened            1   1.301  1.301 
13  apple                1   0.699  0.699 
14  citrus               1   1.000  1.000 
15  sage                 1   1.301  1.301 
16  brisk                1   1.000  1.000 
17  acidity              1   0.398  0.398 
---------------------------------------------------------------

# Documento 1

Terminos analizados del documento >> 15 palabras
N.  Termino              TF  IDF    TF-IDF
1   acidity              1   0.398  0.398 
2   ripe                 1   0.824  0.824 
3   fruity               1   1.000  1.000 
4   wine                 1   0.398  0.398 
5   smooth               1   1.301  1.301 
6   structured           1   1.301  1.301 
7   firm                 1   0.824  0.824 
8   tannins              1   0.824  0.824 
9   fill                 1   1.301  1.301 
10  juicy                1   0.824  0.824 
11  berry                1   1.000  1.000 
12  fruits               1   0.824  0.824 
13  freshened            1   1.301  1.301 
14  drinkable            1   1.301  1.301 
15  2016                 1   1.301  1.301 
---------------------------------------------------------------

# Documento 2

Terminos analizados del documento >> 17 palabras
N.  Termino              TF  IDF    TF-IDF
1   acidity              1   0.398  0.398 
2   wine                 1   0.398  0.398 
3   tart                 1   0.824  0.824 
4   snappy               1   1.301  1.301 
5   flavors              2   0.523  1.046 
6   lime                 1   1.301  1.301 
7   flesh                1   1.301  1.301 
8   rind                 1   1.000  1.000 
9   dominate             1   0.824  0.824 
10  green                1   0.699  0.699 
11  pineapple            1   0.824  0.824 
12  pokes                1   1.301  1.301 
13  crisp                1   0.824  0.824 
14  underscoring         1   1.301  1.301 
15  stainless-steel      1   1.301  1.301 
16  fermented            1   1.301  1.301 
---------------------------------------------------------------

# Documento 3

Terminos analizados del documento >> 20 palabras
N.  Termino              TF  IDF    TF-IDF
1   aromas               1   0.301  0.301 
2   palate               1   0.398  0.398 
3   rind                 1   1.000  1.000 
4   pineapple            1   0.824  0.824 
5   lemon                1   1.301  1.301 
6   pith                 1   1.301  1.301 
7   orange               1   1.000  1.000 
8   blossom              1   1.301  1.301 
9   start                1   1.301  1.301 
10  bite                 1   1.000  1.000 
11  opulent              1   1.301  1.301 
12  note                 1   0.602  0.602 
13  honey-drizzled       1   1.301  1.301 
14  guava                1   1.301  1.301 
15  mango                1   1.301  1.301 
16  give                 1   1.301  1.301 
17  slightly             1   0.824  0.824 
18  astringent           1   1.000  1.000 
19  semidry              1   1.301  1.301 
20  finish               1   0.523  0.523 
---------------------------------------------------------------

# Documento 4

Terminos analizados del documento >> 17 palabras
N.  Termino              TF  IDF    TF-IDF
1   wine                 1   0.398  0.398 
2   regular              1   1.301  1.301 
3   bottling             1   1.301  1.301 
4   2012                 1   1.301  1.301 
5   tannic               1   0.824  0.824 
6   rustic               1   1.301  1.301 
7   earthy               1   1.301  1.301 
8   herbal               1   1.000  1.000 
9   characteristics      1   1.301  1.301 
10  pleasantly           1   1.301  1.301 
11  unfussy              1   1.301  1.301 
12  country              1   1.301  1.301 
13  good                 1   0.824  0.824 
14  companion            1   1.301  1.301 
15  hearty               1   1.301  1.301 
16  winter               1   1.301  1.301 
17  stew                 1   1.301  1.301 
---------------------------------------------------------------

# Documento 5

Terminos analizados del documento >> 25 palabras
N.  Termino              TF  IDF    TF-IDF
1   aromas               1   0.301  0.301 
2   acidity              1   0.398  0.398 
3   flavors              1   0.523  0.523 
4   green                1   0.699  0.699 
5   finish               1   0.523  0.523 
6   herbal               1   1.000  1.000 
7   blackberry           1   1.000  1.000 
8   raspberry            1   1.301  1.301 
9   show                 1   1.301  1.301 
10  typical              1   1.301  1.301 
11  navarran             1   1.301  1.301 
12  whiff                1   1.301  1.301 
13  herbs                1   1.301  1.301 
14  case                 1   1.301  1.301 
15  horseradish          1   1.301  1.301 
16  mouth                1   1.301  1.301 
17  bodied               1   1.301  1.301 
18  tomatoey             1   1.301  1.301 
19  spicy                1   1.000  1.000 
20  complement           1   1.301  1.301 
21  dark                 1   1.000  1.000 
22  plum                 1   0.699  0.699 
23  fruit                1   0.824  0.824 
24  fresh                1   0.699  0.699 
25  grabby               1   1.301  1.301 
---------------------------------------------------------------

# Documento 6

Terminos analizados del documento >> 17 palabras
N.  Termino              TF  IDF    TF-IDF
1   aromas               1   0.301  0.301 
2   herb                 1   1.000  1.000 
3   palate               1   0.398  0.398 
4   acidity              1   0.398  0.398 
5   tannins              1   0.824  0.824 
6   berry                1   1.000  1.000 
7   fresh                1   0.699  0.699 
8   bright               1   1.301  1.301 
9   informal             1   1.301  1.301 
10  open                 1   1.000  1.000 
11  candied              1   1.301  1.301 
12  white                1   1.301  1.301 
13  pepper               1   0.699  0.699 
14  savory               1   1.000  1.000 
15  carry                1   0.824  0.824 
16  balance              1   0.699  0.699 
17  soft                 1   1.301  1.301 
---------------------------------------------------------------

# Documento 7

Terminos analizados del documento >> 11 palabras
N.  Termino              TF  IDF    TF-IDF
1   offer                1   0.699  0.699 
2   acidity              1   0.398  0.398 
3   wine                 1   0.398  0.398 
4   firm                 1   0.824  0.824 
5   balance              1   0.699  0.699 
6   dry                  1   0.699  0.699 
7   restrain             1   1.000  1.000 
8   spice                1   1.000  1.000 
9   profusion            1   1.301  1.301 
10  texture              1   0.824  0.824 
11  food                 1   1.000  1.000 
---------------------------------------------------------------

# Documento 8

Terminos analizados del documento >> 17 palabras
N.  Termino              TF  IDF    TF-IDF
1   dried                1   1.000  1.000 
2   brisk                1   1.000  1.000 
3   fruity               1   1.000  1.000 
4   wine                 1   0.398  0.398 
5   flavors              1   0.523  0.523 
6   note                 1   0.602  0.602 
7   fresh                1   0.699  0.699 
8   savory               1   1.000  1.000 
9   thyme                1   1.301  1.301 
10  accent               1   1.301  1.301 
11  sunnier              1   1.301  1.301 
12  preserve             1   1.301  1.301 
13  peach                1   1.301  1.301 
14  off-dry              1   1.301  1.301 
15  elegant              1   1.301  1.301 
16  sprightly            1   1.000  1.000 
17  footprint            1   1.301  1.301 
---------------------------------------------------------------

# Documento 9

Terminos analizados del documento >> 14 palabras
N.  Termino              TF  IDF    TF-IDF
1   apple                1   0.699  0.699 
2   acidity              1   0.398  0.398 
3   fruits               1   0.824  0.824 
4   crisp                1   0.824  0.824 
5   fresh                1   0.699  0.699 
6   balance              1   0.699  0.699 
7   dry                  1   0.699  0.699 
8   spice                1   1.000  1.000 
9   texture              1   0.824  0.824 
10  great                1   1.301  1.301 
11  depth                1   1.301  1.301 
12  flavor               1   0.824  0.824 
13  touch                1   1.301  1.301 
14  drink                1   1.301  1.301 
---------------------------------------------------------------

# Documento 10

Terminos analizados del documento >> 16 palabras
N.  Termino              TF  IDF    TF-IDF
1   citrus               1   1.000  1.000 
2   wine                 2   0.398  0.796 
3   crisp                1   0.824  0.824 
4   spicy                1   1.000  1.000 
5   pepper               1   0.699  0.699 
6   dry                  1   0.699  0.699 
7   texture              1   0.824  0.824 
8   food                 1   1.000  1.000 
9   tight                1   1.301  1.301 
10  taut                 1   1.301  1.301 
11  strongly             1   1.301  1.301 
12  mineral              1   1.301  1.301 
13  character            1   1.000  1.000 
14  layered              1   1.301  1.301 
15  aftertaste           1   1.301  1.301 
---------------------------------------------------------------

# Documento 11

Terminos analizados del documento >> 17 palabras
N.  Termino              TF  IDF    TF-IDF
1   offer                1   0.699  0.699 
2   wine                 1   0.398  0.398 
3   firm                 1   0.824  0.824 
4   juicy                1   0.824  0.824 
5   slightly             1   0.824  0.824 
6   tannic               1   0.824  0.824 
7   reduce               1   1.301  1.301 
8   chalky               1   1.301  1.301 
9   backbone             1   1.301  1.301 
10  explosion            1   1.301  1.301 
11  rich                 1   1.301  1.301 
12  black                1   1.000  1.000 
13  cherry               1   1.000  1.000 
14  accented             1   1.301  1.301 
15  oak                  1   0.699  0.699 
16  cigar                1   1.000  1.000 
17  box                  1   1.000  1.000 
---------------------------------------------------------------

# Documento 12

Terminos analizados del documento >> 20 palabras
N.  Termino              TF  IDF    TF-IDF
1   aromas               1   0.301  0.301 
2   include              1   1.000  1.000 
3   palate               1   0.398  0.398 
4   tannins              1   0.824  0.824 
5   dominate             1   0.824  0.824 
6   astringent           1   1.000  1.000 
7   finish               1   0.523  0.523 
8   plum                 1   0.699  0.699 
9   carry                1   0.824  0.824 
10  oak                  1   0.699  0.699 
11  oak-driven           1   1.000  1.000 
12  roasted              1   1.301  1.301 
13  coffee               1   1.301  1.301 
14  bean                 1   1.301  1.301 
15  espresso             1   1.301  1.301 
16  coconut              1   1.301  1.301 
17  vanilla              1   1.000  1.000 
18  chocolate            1   1.301  1.301 
19  drying               1   1.301  1.301 
20  abrupt               1   1.301  1.301 
---------------------------------------------------------------

# Documento 13

Terminos analizados del documento >> 30 palabras
N.  Termino              TF  IDF    TF-IDF
1   apple                1   0.699  0.699 
2   ripe                 1   0.824  0.824 
3   wine                 1   0.398  0.398 
4   tart                 1   0.824  0.824 
5   flavors              1   0.523  0.523 
6   green                1   0.699  0.699 
7   pineapple            1   0.824  0.824 
8   good                 1   0.824  0.824 
9   build                1   1.301  1.301 
10  150                  1   1.301  1.301 
11  years                1   1.301  1.301 
12  generations          1   1.301  1.301 
13  winemaking           1   1.301  1.301 
14  tradition            1   1.301  1.301 
15  winery               1   1.301  1.301 
16  trends               1   1.301  1.301 
17  leaner               1   1.301  1.301 
18  style                1   1.301  1.301 
19  classic              1   1.301  1.301 
20  california           1   1.301  1.301 
21  buttercream          1   1.301  1.301 
22  aroma                1   1.301  1.301 
23  cut                  1   1.301  1.301 
24  everyday             1   1.301  1.301 
25  sipping              1   1.301  1.301 
26  range                1   1.301  1.301 
27  barely               1   1.301  1.301 
28  prove                1   1.301  1.301 
29  approachable         1   1.000  1.000 
30  distinctive          1   1.301  1.301 
---------------------------------------------------------------

# Documento 14

Terminos analizados del documento >> 18 palabras
N.  Termino              TF  IDF    TF-IDF
1   palate               1   0.398  0.398 
2   apple                1   0.699  0.699 
3   orange               1   1.000  1.000 
4   note                 1   0.602  0.602 
5   dry                  1   0.699  0.699 
6   sprightly            1   1.000  1.000 
7   zesty                1   1.301  1.301 
8   peels                1   1.301  1.301 
9   abound               1   1.301  1.301 
10  mineral-toned        1   1.301  1.301 
11  riesling             1   1.301  1.301 
12  racy                 1   1.301  1.301 
13  lean                 1   1.301  1.301 
14  refreshing           1   1.301  1.301 
15  easy                 1   1.301  1.301 
16  quaffer              1   1.301  1.301 
17  wide                 1   1.301  1.301 
18  appeal               1   1.301  1.301 
---------------------------------------------------------------

# Documento 15

Terminos analizados del documento >> 30 palabras
N.  Termino              TF  IDF    TF-IDF
1   aromas               1   0.301  0.301 
2   palate               1   0.398  0.398 
3   acidity              1   0.398  0.398 
4   flavors              1   0.523  0.523 
5   green                1   0.699  0.699 
6   finish               1   0.523  0.523 
7   plum                 2   0.699  1.398 
8   balance              1   0.699  0.699 
9   flavor               1   0.824  0.824 
10  oak                  1   0.699  0.699 
11  bake                 1   1.301  1.301 
12  molasses             1   1.301  1.301 
13  balsamic             1   1.301  1.301 
14  vinegar              1   1.301  1.301 
15  cheesy               1   1.301  1.301 
16  feed                 1   1.301  1.301 
17  braced               1   1.301  1.301 
18  bolt                 1   1.301  1.301 
19  compact              1   1.301  1.301 
20  set                  1   1.301  1.301 
21  saucy                1   1.301  1.301 
22  red-berry            1   1.301  1.301 
23  feature              1   1.301  1.301 
24  tobacco              1   1.000  1.000 
25  peppery              1   1.301  1.301 
26  accents              1   1.301  1.301 
27  mildly               1   1.301  1.301 
28  respectable          1   1.301  1.301 
29  weight               1   1.301  1.301 
---------------------------------------------------------------

# Documento 16

Terminos analizados del documento >> 22 palabras
N.  Termino              TF  IDF    TF-IDF
1   aromas               1   0.301  0.301 
2   juicy                1   0.824  0.824 
3   fruits               1   0.824  0.824 
4   finish               1   0.523  0.523 
5   good                 1   0.824  0.824 
6   flavor               1   0.824  0.824 
7   character            1   1.000  1.000 
8   oak                  2   0.699  1.398 
9   raw                  1   1.301  1.301 
10  black-cherry         1   1.301  1.301 
11  simple               1   1.301  1.301 
12  feel                 1   1.301  1.301 
13  thickens             1   1.301  1.301 
14  extract              1   1.301  1.301 
15  apparent             1   1.301  1.301 
16  profile              1   1.301  1.301 
17  drive                1   1.301  1.301 
18  dark-berry           1   1.301  1.301 
19  smoldering           1   1.301  1.301 
20  meaty                1   1.301  1.301 
21  hot                  1   1.301  1.301 
---------------------------------------------------------------

# Documento 17

Terminos analizados del documento >> 28 palabras
N.  Termino              TF  IDF    TF-IDF
1   aromas               2   0.301  0.602 
2   flavors              1   0.523  0.523 
3   dominate             1   0.824  0.824 
4   finish               1   0.523  0.523 
5   tannic               1   0.824  0.824 
6   blackberry           2   1.000  2.000 
7   fruit                1   0.824  0.824 
8   carry                1   0.824  0.824 
9   desiccated           1   1.301  1.301 
10  leather              1   1.301  1.301 
11  charred              1   1.301  1.301 
12  wood                 1   1.301  1.301 
13  mint                 1   1.301  1.301 
14  nose                 1   1.000  1.000 
15  full-bodied          1   1.301  1.301 
16  heavily              1   1.301  1.301 
17  oaked                1   1.301  1.301 
18  tinto                1   1.301  1.301 
19  fino                 1   1.301  1.301 
20  clove                1   1.301  1.301 
21  woodspice            1   1.301  1.301 
22  top                  1   1.301  1.301 
23  hickory              1   1.301  1.301 
24  forceful             1   1.301  1.301 
25  oak-based            1   1.301  1.301 
26  rise                 1   1.301  1.301 
---------------------------------------------------------------

# Documento 18

Terminos analizados del documento >> 29 palabras
N.  Termino              TF  IDF    TF-IDF
1   aromas               1   0.301  0.301 
2   palate               1   0.398  0.398 
3   note                 2   0.602  1.204 
4   slightly             1   0.824  0.824 
5   plum                 1   0.699  0.699 
6   fruit                1   0.824  0.824 
7   open                 1   1.000  1.000 
8   pepper               1   0.699  0.699 
9   restrain             1   1.000  1.000 
10  cherry               1   1.000  1.000 
11  cigar                1   1.000  1.000 
12  box                  1   1.000  1.000 
13  approachable         1   1.000  1.000 
14  nose                 1   1.000  1.000 
15  pervade              1   1.301  1.301 
16  menthol              1   1.301  1.301 
17  ride                 1   1.301  1.301 
18  entry                1   1.301  1.301 
19  riper                1   1.301  1.301 
20  specked              1   1.301  1.301 
21  crushed              1   1.301  1.301 
22  blend                1   1.301  1.301 
23  merlot               1   1.301  1.301 
24  cabernet             2   1.301  2.602 
25  sauvignon            1   1.301  1.301 
26  franc                1   1.301  1.301 
27  enjoy                1   1.301  1.301 
---------------------------------------------------------------

# Documento 19

Terminos analizados del documento >> 22 palabras
N.  Termino              TF  IDF    TF-IDF
1   aromas               1   0.301  0.301 
2   palate               1   0.398  0.398 
3   offer                1   0.699  0.699 
4   ripe                 1   0.824  0.824 
5   tart                 1   0.824  0.824 
6   bite                 1   1.000  1.000 
7   note                 2   0.602  1.204 
8   dark                 1   1.000  1.000 
9   pepper               1   0.699  0.699 
10  black                1   1.000  1.000 
11  oak-driven           1   1.000  1.000 
12  vanilla              1   1.000  1.000 
13  tobacco              1   1.000  1.000 
14  berries              1   1.301  1.301 
15  mingle               1   1.301  1.301 
16  toasted              1   1.301  1.301 
17  dusty                1   1.301  1.301 
18  nature               1   1.301  1.301 
19  currant              1   1.301  1.301 
20  shine                1   1.301  1.301 
21  levity               1   1.301  1.301 
---------------------------------------------------------------

SIMILITUD ENTRE DOCUMENTOS

           [D.0]    [D.1]    [D.2]    [D.3]    [D.4]    [D.5]    [D.6]    [D.7]    [D.8]    [D.9]    [D.10]   [D.11]   [D.12]   [D.13]   [D.14]   [D.15]   [D.16]   [D.17]   [D.18]   [D.19]   
[Doc 0] -> 1.000    0.009    0.008    0.011    0.000    0.010    0.077    0.050    0.146    0.040    0.052    0.025    0.059    0.017    0.029    0.015    0.004    0.006    0.009    0.033    
[Doc 1] -> 0.009    1.000    0.019    0.000    0.008    0.007    0.116    0.089    0.065    0.059    0.019    0.090    0.037    0.033    0.000    0.007    0.064    0.000    0.000    0.035    
[Doc 2] -> 0.008    0.019    1.000    0.083    0.008    0.053    0.010    0.027    0.038    0.056    0.058    0.009    0.035    0.096    0.000    0.047    0.000    0.048    0.000    0.033    
[Doc 3] -> 0.011    0.000    0.083    1.000    0.000    0.014    0.013    0.000    0.017    0.000    0.000    0.033    0.069    0.022    0.065    0.018    0.014    0.015    0.056    0.084    
[Doc 4] -> 0.000    0.008    0.008    0.000    1.000    0.038    0.000    0.011    0.007    0.000    0.015    0.040    0.000    0.027    0.000    0.000    0.026    0.022    0.000    0.000    
[Doc 5] -> 0.010    0.007    0.053    0.014    0.038    1.000    0.035    0.011    0.032    0.034    0.045    0.000    0.035    0.022    0.000    0.070    0.013    0.104    0.038    0.042    
[Doc 6] -> 0.077    0.116    0.010    0.013    0.000    0.035    1.000    0.058    0.084    0.081    0.030    0.000    0.088    0.000    0.008    0.037    0.004    0.035    0.071    0.038    
[Doc 7] -> 0.050    0.089    0.027    0.000    0.011    0.011    0.058    1.000    0.013    0.283    0.214    0.112    0.000    0.009    0.036    0.038    0.000    0.000    0.058    0.036    
[Doc 8] -> 0.146    0.065    0.038    0.017    0.007    0.032    0.084    0.013    1.000    0.031    0.017    0.008    0.000    0.015    0.063    0.010    0.000    0.010    0.026    0.034    
[Doc 9] -> 0.040    0.059    0.056    0.000    0.000    0.034    0.081    0.283    0.031    1.000    0.126    0.000    0.000    0.022    0.056    0.062    0.072    0.000    0.000    0.000    
[Doc 10] ->0.052    0.019    0.058    0.000    0.015    0.045    0.030    0.214    0.017    0.126    1.000    0.018    0.000    0.012    0.024    0.000    0.046    0.000    0.019    0.024    
[Doc 11] ->0.025    0.090    0.009    0.033    0.040    0.000    0.000    0.112    0.008    0.000    0.018    1.000    0.025    0.006    0.000    0.019    0.074    0.026    0.140    0.072    
[Doc 12] ->0.059    0.037    0.035    0.069    0.000    0.035    0.088    0.000    0.000    0.000    0.000    0.025    1.000    0.000    0.007    0.072    0.055    0.065    0.026    0.101    
[Doc 13] ->0.017    0.033    0.096    0.022    0.027    0.022    0.000    0.009    0.015    0.022    0.012    0.006    0.000    1.000    0.016    0.020    0.020    0.007    0.025    0.044    
[Doc 14] ->0.029    0.000    0.000    0.065    0.000    0.000    0.008    0.036    0.063    0.056    0.024    0.000    0.007    0.016    1.000    0.005    0.000    0.000    0.029    0.037    
[Doc 15] ->0.015    0.007    0.047    0.018    0.000    0.070    0.037    0.038    0.010    0.062    0.000    0.019    0.072    0.020    0.005    1.000    0.063    0.020    0.033    0.043    
[Doc 16] ->0.004    0.064    0.000    0.014    0.026    0.013    0.004    0.000    0.000    0.072    0.046    0.074    0.055    0.020    0.000    0.063    1.000    0.014    0.003    0.004    
[Doc 17] ->0.006    0.000    0.048    0.015    0.022    0.104    0.035    0.000    0.010    0.000    0.000    0.026    0.065    0.007    0.000    0.020    0.014    1.000    0.049    0.006    
[Doc 18] ->0.009    0.000    0.000    0.056    0.000    0.038    0.071    0.058    0.026    0.000    0.019    0.140    0.026    0.025    0.029    0.033    0.003    0.049    1.000    0.073    
[Doc 19] ->0.033    0.035    0.033    0.084    0.000    0.042    0.038    0.036    0.034    0.000    0.024    0.072    0.101    0.044    0.037    0.043    0.004    0.006    0.073    1.000    
```

--- 

# Conclusión.

La práctica de construir un sistema de recomendación basado en el contenido ha permitido aplicar técnicas de procesamiento de lenguaje natural como el cálculo de TF, IDF y TF-IDF, esenciales para representar la relevancia de los términos en los documentos. Además, se ha implementado el cálculo de similitud entre documentos utilizando la similitud del coseno, lo que permite recomendar documentos similares a los usuarios en función de su contenido. Este enfoque es útil en áreas como la recomendación de artículos, libros o productos, así como en la clasificación y análisis de texto.

El sistema también incluye un flujo de trabajo eficiente para el procesamiento de texto, que abarca la eliminación de stopwords, la lematización de términos y la eliminación de redundancias. A través de una interfaz de línea de comandos, el programa ofrece flexibilidad para analizar documentos, visualizar los resultados o guardarlos en archivos. Este tipo de modelos es clave para la personalización de servicios y mejora de la experiencia de usuario en plataformas que manejan grandes volúmenes de contenido textual.