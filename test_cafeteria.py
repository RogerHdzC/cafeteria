import pytest
import json
from cafeteria import Cafeteria

# Fixture para crear una instancia de Cafeteria para pruebas
@pytest.fixture
def cafeteria(tmp_path):
    archivo_json = tmp_path / "datos_cafeteria.json"
    with open(archivo_json, "w") as f:
        json.dump({}, f)  # Crear un archivo JSON vacío para pruebas
    return Cafeteria(str(archivo_json))

# Casos de prueba para el método agregar_bebida

def test_agregar_bebida_nombre_valido(cafeteria):
    assert cafeteria.agregar_bebida("Latte, 12, 16, 20") == "Bebida agregada correctamente."

def test_agregar_bebida_nombre_invalido_longitud_minima(cafeteria):
    assert cafeteria.agregar_bebida("A, 12, 16, 20") == "Error: El nombre del artículo debe contener caracteres alfabéticos y tener una longitud de 2 a 15 caracteres."

def test_agregar_bebida_nombre_invalido_longitud_maxima(cafeteria):
    assert cafeteria.agregar_bebida("EsteNombreEsDemasiadoLargo, 12, 16, 20") == "Error: El nombre del artículo debe contener caracteres alfabéticos y tener una longitud de 2 a 15 caracteres."

def test_agregar_bebida_tamano_valido(cafeteria):
    assert cafeteria.agregar_bebida("Mocha, 12, 16, 20") == "Bebida agregada correctamente."

def test_agregar_bebida_tamano_invalido_valor_fuera_de_rango(cafeteria):
    assert cafeteria.agregar_bebida("Café, 50, 16, 20") == "Error: Los tamaños deben ser valores enteros dentro del rango de 1 a 48 y deben estar en orden ascendente."

def test_agregar_bebida_tamano_invalido_no_entero(cafeteria):
    assert cafeteria.agregar_bebida("Té, 12, 16, x") == "Error: Los tamaños deben ser valores enteros dentro del rango de 1 a 48 y deben estar en orden ascendente."

def test_agregar_bebida_tamano_invalido_no_orden_ascendente(cafeteria):
    assert cafeteria.agregar_bebida("Capuchino, 20, 16, 12") == "Error: Los tamaños deben ser valores enteros dentro del rango de 1 a 48 y deben estar en orden ascendente."

def test_agregar_bebida_un_solo_tamano(cafeteria):
    assert cafeteria.agregar_bebida("Americano, 12") == "Bebida agregada correctamente."

def test_agregar_bebida_mas_de_cinco_tamanos(cafeteria):
    assert cafeteria.agregar_bebida("Chocolate, 12, 16, 20, 24, 30, 36") == "Error: La bebida ya tiene el máximo de 5 tamaños permitidos."

def test_agregar_bebida_formato_invalido_falta_coma(cafeteria):
    assert cafeteria.agregar_bebida("Café con leche 12, 16, 20") == "Error: El nombre del artículo debe contener caracteres alfabéticos y tener una longitud de 2 a 15 caracteres."

def test_agregar_bebida_formato_invalido_sobran_comas(cafeteria):
    assert cafeteria.agregar_bebida("Café, con, leche, 12, 16, 20") == "Error: Los tamaños deben ser valores enteros dentro del rango de 1 a 48 y deben estar en orden ascendente."

def test_agregar_bebida_formato_invalido_nombre_numerico(cafeteria):
    assert cafeteria.agregar_bebida("123, 12, 16, 20") == "Error: El nombre del artículo debe contener caracteres alfabéticos y tener una longitud de 2 a 15 caracteres."

def test_agregar_bebida_formato_invalido_tamano_letras(cafeteria):
    assert cafeteria.agregar_bebida("Té, doce, 16, 20") == "Error: Los tamaños deben ser valores enteros dentro del rango de 1 a 48 y deben estar en orden ascendente."

def test_agregar_bebida_formato_invalido_tamano_vacios(cafeteria):
    assert cafeteria.agregar_bebida("Té, , 16, 20") == "Error: Los tamaños deben ser valores enteros dentro del rango de 1 a 48 y deben estar en orden ascendente."

def test_agregar_bebida_formato_invalido_tamano_demasiados_ceros(cafeteria):
    assert cafeteria.agregar_bebida("Té, 00, 16, 20") == "Error: Los tamaños deben ser valores enteros dentro del rango de 1 a 48 y deben estar en orden ascendente."

def test_agregar_bebida_formato_invalido_tamano_negativo(cafeteria):
    assert cafeteria.agregar_bebida("Té, -5, 16, 20") == "Error: Los tamaños deben ser valores enteros dentro del rango de 1 a 48 y deben estar en orden ascendente."

def test_agregar_bebida_formato_invalido_tamano_decimal(cafeteria):
    assert cafeteria.agregar_bebida("Té, 12.5, 16, 20") == "Error: Los tamaños deben ser valores enteros dentro del rango de 1 a 48 y deben estar en orden ascendente."

def test_agregar_bebida_nombre_duplicado_misma_mayuscula(cafeteria):
    cafeteria.agregar_bebida("Latte, 12, 16, 20")
    assert cafeteria.agregar_bebida("Latte, 12, 16, 20") == "Error: La bebida ya existe en el sistema."

def test_agregar_bebida_nombre_duplicado_diferente_mayuscula(cafeteria):
    cafeteria.agregar_bebida("Mocha, 12, 16, 20")
    assert cafeteria.agregar_bebida("mocha, 12, 16, 20") == "Error: La bebida ya existe en el sistema."

def test_agregar_bebida_nombre_duplicado_nuevos_tamanos(cafeteria):
    cafeteria.agregar_bebida("Cappuccino, 12, 16, 20")
    assert cafeteria.agregar_bebida("cappuccino, 12, 16, 20, 24, 30") == "La bebida ya existe, se agregaron los tamaños extras: 12, 16, 20, 24, 30"

def test_agregar_bebida_nombre_duplicado_tamanos_extra(cafeteria):
    cafeteria.agregar_bebida("Cappuccino, 12, 16, 20")
    cafeteria.agregar_bebida("Cappuccino, 12, 16, 20, 24, 30")
    assert cafeteria.agregar_bebida("cappuccino, 12, 16, 48") == "Error: La bebida ya tiene el máximo de 5 tamaños permitidos."
