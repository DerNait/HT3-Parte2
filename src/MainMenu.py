import SortsMain
import cProfile
import sys

'''
Se le pregunto a la IA lo siguiente: Como hago un cProfile para mi siguiente codigo: [Se inserto el codigo del menu aquí]
'''

def mostrar_menu():
    print("1. Comenzar a ordenar los números")
    print("2. Salir")

def elegir_direccion():
    print("¿Cómo desea ordenar los números?")
    print("1. Ascendente")
    print("2. Descendente")
    opcion = input("Seleccione una opción (1/2): ")
    return opcion

def ordenar_numeros_con_perfil(direccion_str):
    # Esta es la función que se perfilará si se activa el modo de perfilado.
    SortsMain.ordenar_numeros_main(direccion_str)

def main(perfilado=False):
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            direccion = elegir_direccion()
            direccion_str = 'ascendente' if direccion == "1" else 'descendente'
            
            if perfilado:
                # Ejecutar con perfilado
                cProfile.runctx('ordenar_numeros_con_perfil(direccion_str)', globals(), locals())
            else:
                # Ejecución normal
                SortsMain.ordenar_numeros_main(direccion_str)

        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    perfilado = '--perfil' in sys.argv  # Comprobar si se ha pasado el argumento '--perfil'
    main(perfilado)
