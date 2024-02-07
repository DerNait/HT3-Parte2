# Importar los algoritmos de ordenamiento
from gnome import gnome_sort
from headsort import heap_sort
from mergeSort import merge_sort
from quicksort import quicksort
from selection1 import selection_sort
from shellSort import shell_sort
from countingSort import radixSort

# Función para cargar números desde un archivo
def cargar_numeros(archivo):
    with open(archivo, 'r') as f:
        numeros = [int(line.strip()) for line in f.readlines()]
    return numeros

# Modificar la lista de funciones para envolver quicksort en una función lambda o definida por el usuario
def ordenar_numeros(numeros):
    sort_functions = [
        ("Gnome Sort", gnome_sort),
        ("Heap Sort", heap_sort),
        ("Merge Sort", merge_sort),
        # Envolver quicksort en una lambda que solo toma la lista como argumento
        ("Quick Sort", lambda arr: quicksort(arr, 0, len(arr) - 1)),
        ("Selection Sort", selection_sort),
        ("Shell Sort", shell_sort),
        ("Counting Sort", radixSort)
    ]

    resultados = {}
    for nombre, funcion in sort_functions:
        copia_numeros = numeros[:]  # Hacer una copia para no modificar la lista original
        if nombre != "Quick Sort":  # Quick Sort ya fue ejecutado durante la definición de la lambda
            funcion(copia_numeros)  # Se asume que la función modifica la lista in-place
        resultados[nombre] = copia_numeros
    return resultados


# Main
if __name__ == "__main__":
    archivo_numeros = "numeros_aleatorios.txt"  # Asegúrate de ajustar el nombre de archivo según corresponda
    numeros = cargar_numeros(archivo_numeros)
    resultados = ordenar_numeros(numeros)

    # Opcional: imprimir los resultados
    for nombre, numeros_ordenados in resultados.items():
        print(f"{nombre}: {numeros_ordenados[:10]}...")  # Imprime solo los primeros 10 para brevedad
