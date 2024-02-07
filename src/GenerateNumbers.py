import random

'''
Se pregunto a la IA lo siguiente para guardar en un archivo numeros aleatorios:
Genera un codigo que genere 3000 numeros del 0 al 10000 y que los guarde en un archivo txt
'''

def generar_numeros_aleatorios(filename, cantidad=3000, minimo=0, maximo=10000):
    with open(filename, 'w') as f:
        for _ in range(cantidad):
            f.write(f"{random.randint(minimo, maximo)}\n")

generar_numeros_aleatorios('numeros_aleatorios.txt')
