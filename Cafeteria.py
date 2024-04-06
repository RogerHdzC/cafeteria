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
        
        # Verificar los tamaños
        try:
            nombre = partes[0].strip().lower()  # Convertir el nombre a minúsculas
            tamanos = partes[1].split(',')
            tamanos = list(map(int, tamanos))
        except ValueError:
            return "Error: Los tamaños deben ser valores enteros dentro del rango de 1 a 48 y deben estar en orden ascendente."
        
        if len(tamanos) > 5:
             return "Error: La bebida ya tiene el máximo de 5 tamaños permitidos."

        if not all(1 <= tam <= 48 for tam in tamanos) or tamanos != sorted(tamanos):
            return "Error: Los tamaños deben ser valores enteros dentro del rango de 1 a 48 y deben estar en orden ascendente."

        # Verificar el nombre del artículo
        if not nombre.isalpha() or len(nombre) < 2 or len(nombre) > 15:
            return "Error: El nombre del artículo debe contener caracteres alfabéticos y tener una longitud de 2 a 15 caracteres."

        # Verificar si el nombre ya existe (sin importar mayúsculas o minúsculas)
        nombre_existente = next((bebida_nombre for bebida_nombre in self.bebidas.keys() if bebida_nombre.lower() == nombre), None)

        if nombre_existente:
            # Combinar tamaños si la bebida ya existe
            tamanos_existente = self.bebidas[nombre_existente]
            nuevos_tamanos = sorted(set(tamanos_existente + tamanos))
            if len(nuevos_tamanos) > 5:
                return "Error: La bebida ya tiene el máximo de 5 tamaños permitidos."
            if nuevos_tamanos == tamanos_existente:
                return "Error: La bebida ya existe en el sistema."
            else:
                self.bebidas[nombre_existente] = nuevos_tamanos
                self.guardar_bebidas()
                return f"La bebida ya existe, se agregaron los tamaños extras: {', '.join(map(str, nuevos_tamanos))}"

        # Agregar la bebida al diccionario de bebidas
        self.bebidas[nombre] = tamanos
        self.guardar_bebidas()  # Guardar los datos actualizados en el archivo JSON
        return "Bebida agregada correctamente."