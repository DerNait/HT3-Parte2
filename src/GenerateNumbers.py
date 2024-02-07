import random

def generar_numeros_aleatorios(filename, cantidad=3000, minimo=0, maximo=10000):
    with open(filename, 'w') as f:
        for _ in range(cantidad):
            f.write(f"{random.randint(minimo, maximo)}\n")

generar_numeros_aleatorios('numeros_aleatorios.txt')
