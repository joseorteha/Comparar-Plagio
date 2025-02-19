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