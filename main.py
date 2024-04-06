from Cafeteria import Cafeteria

def main():
    archivo_json = "datos_cafeteria.json"
    cafeteria = Cafeteria(archivo_json)

    # Mostrar las bebidas actuales antes de mostrar el menú
    print("Bebidas actuales:")
    for bebida, tamanos in cafeteria.bebidas.items():
        print(f"{bebida}: {', '.join(map(str, tamanos))}")

if __name__ == "__main__":
    main()
