import json
import re

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