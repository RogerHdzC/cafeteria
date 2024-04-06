import json

class Cafeteria:
    def __init__(self, archivo):
        self.archivo = archivo
        self.bebidas = self.cargar_bebidas()

    def cargar_bebidas(self):
        try:
            with open(self.archivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def guardar_bebidas(self):
        with open(self.archivo, 'w') as f:
            json.dump(self.bebidas, f, indent=4)

    def agregar_bebida(self, entrada):
        # Eliminar todos los espacios en blanco de la entrada
        entrada = entrada.replace(" ", "")
        
        # Separar el nombre del artículo y los tamaños
        partes = entrada.split(',', maxsplit=1)  # Solo dividir la entrada en dos partes
        
        if len(partes) < 2:
            return "Error: Formato de entrada inválido."  # No hay suficientes partes después de dividir por comas
        
        nombre = partes[0].strip()  
        tamanos = partes[1].split(',')
        tamanos = list(map(int, tamanos))
        
        # Agregar la bebida al diccionario de bebidas
        self.bebidas[nombre] = tamanos
        self.guardar_bebidas()  # Guardar los datos actualizados en el archivo JSON
        return "Bebida agregada correctamente."