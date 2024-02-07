import SortsMain

def mostrar_menu():
    print("1. Comenzar a ordenar los números")
    print("2. Salir")

def elegir_direccion():
    print("¿Cómo desea ordenar los números?")
    print("1. Ascendente")
    print("2. Descendente")
    opcion = input("Seleccione una opción (1/2): ")
    return opcion

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            direccion = elegir_direccion()
            direccion_str = 'ascendente' if direccion == "1" else 'descendente'
            SortsMain.ordenar_numeros_main(direccion_str)

        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()