# Comparador de Plagio

![GitHub Logo](https://github.com/favicon.ico)

## Descripción

Este repositorio contiene un script en Python llamado `plagio.py`, diseñado para comparar dos archivos de texto y determinar el porcentaje de similitud entre ellos. Es una herramienta útil para detectar posibles casos de plagio o simplemente para comparar la similitud entre dos documentos.

## Características

- **Comparación de textos:** Calcula el porcentaje de similitud entre dos archivos de texto.
- **Fácil de usar:** Solo necesitas especificar las rutas de los archivos que deseas comparar.
- **Precisión:** Utiliza el módulo `difflib` de Python para realizar una comparación precisa.

## Requisitos

Para ejecutar este script, necesitarás tener instalado Python 3.x en tu sistema. Además, asegúrate de tener el módulo `difflib`, que viene preinstalado con Python.

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/joseorteha/Comparar-Plagio.git
   
## Uso

1. Ejecuta el script:
      ```bash
      
     python plagiarism_checker.py
     
3. Ingresa las rutas de los dos archivos que deseas comparar cuando se te solicite:
    ```bash
    Enter file_1 path: ruta/del/primer/archivo
    Enter file_2 path: ruta/del/segundo/archivo
El script calculará y mostrará el porcentaje de similitud entre los dos archivos.

## Codigo del script
```
from difflib import SequenceMatcher

def plagiarism_checker(f1, f2):
    # Abrir los archivos y leer sus contenidos
    with open(f1, errors="ignore") as file1, open(f2, errors="ignore") as file2:
        f1_data = file1.read()
        f2_data = file2.read()
    
    # Calcular la similitud entre los archivos
    similarity_ratio = SequenceMatcher(None, f1_data, f2_data).ratio()
    
    # Devolver el porcentaje de similitud
    return similarity_ratio * 100

# Pedir al usuario las rutas de los archivos
f1 = input("Enter file_1 path: ")
f2 = input("Enter file_2 path: ")

# Llamar a la función y obtener el resultado
similarity_percentage = plagiarism_checker(f1, f2)

# Imprimir el resultado
print(f"These files are {similarity_percentage:.2f}% similar")

