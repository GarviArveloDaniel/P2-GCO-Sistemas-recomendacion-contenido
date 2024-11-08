# P2-GCO-Sistemas-recomendacion-contenido


# Integrantes del equipo
- Guillermo Díaz Bricio

- Daniel Garvi Arvelo

- Alexander Morales Díaz

- Alba Pérez Rodríguez


# Introducción.


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


## USO DEL PROGRAMA
Este sistema puede ejecutarse en la terminal mediante:


--- 

# Ejemplos de uso de la aplicación


--- 

# Conclusión.

