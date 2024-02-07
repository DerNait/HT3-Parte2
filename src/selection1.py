'''
Se pregunto a AI:
    Puedes crear un código donde ordene hasta 3000 números al azar, todos enteros de 0 a 1000, con Selection Sort en python?
    Puedes hacer que el usuario pueda elegir si lo quiere ordenar ascendente o descendentemente en este mismo código
    Hola! puedes guardar los números generados en el código anterior en un arreglo?
'''
import random

def selection_sort(arr, ascending=True):
    n = len(arr)

    for i in range(n):
        # Encontrar el índice extremo en el resto de la lista
        extreme_index = i
        for j in range(i+1, n):
            if ascending:
                condition = arr[j] < arr[extreme_index]
            else:
                condition = arr[j] > arr[extreme_index]

            if condition:
                extreme_index = j

        # Intercambiar el elemento extremo encontrado con el primer elemento no ordenado
        arr[i], arr[extreme_index] = arr[extreme_index], arr[i]
