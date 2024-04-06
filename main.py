from Cafeteria import Cafeteria

def main():
    archivo_json = "datos_cafeteria.json"
    cafeteria = Cafeteria(archivo_json)

    while True:
        # Mostrar las bebidas actuales antes de mostrar el menú
        print("Bebidas actuales:")
        for bebida, tamanos in cafeteria.bebidas.items():
            print(f"{bebida}: {', '.join(map(str, tamanos))}")

        # Mostrar el menú
        print("\nMenú:")
        print("1. Agregar nueva bebida")
        print("2. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            entrada = input("Ingrese los detalles de la bebida (nombre, tamaños separados por comas): ")
            resultado = cafeteria.agregar_bebida(entrada)
            print(resultado)
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1 o 2.")

if __name__ == "__main__":
    main()
