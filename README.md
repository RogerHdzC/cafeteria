# Módulo para Cafeterías

Este módulo es parte de un sistema de software para cafeterías que permite la incorporación de nuevas bebidas. Se centra en la lógica de backend que maneja el ingreso de nuevas bebidas y proporciona validación del formato de entrada. La interfaz de usuario (UI) no es una preocupación en este punto.

## Herramientas Utilizadas

- Python 3.12.*
- pytest 8.1.1

## Estructura de Archivos

```
cafeteria/
│
├── cafeteria.py        # Módulo principal que contiene la lógica de backend
├── test_cafeteria.py   # Archivo de pruebas unitarias
└── datos_cafeteria.json  # Archivo JSON que actúa como "base de datos" para las bebidas
```

## Funcionalidades

El módulo `cafeteria.py` proporciona las siguientes funcionalidades:

- `Cafeteria`: Clase principal que gestiona las bebidas en la cafetería.
- `agregar_bebida(entrada)`: Método para agregar nuevas bebidas al sistema, con validación del formato de entrada.

## Ejecución de Pruebas

Para ejecutar las pruebas, asegúrese de tener instalado pytest y luego ejecute el siguiente comando en la raíz del proyecto:

```
pytest
```

## Descripción de Casos de Prueba

### test_agregar_bebida_valida

Este caso de prueba verifica que una bebida válida se agregue correctamente al sistema.

Entrada: `"Latte,12,16,20"`

Resultado esperado: `"Bebida agregada correctamente."`

### test_agregar_bebida_invalida_formato

Este caso de prueba verifica que una entrada con un formato incorrecto no se agregue al sistema.

Entrada: `"Café con leche"`

Resultado esperado: `"Error: Formato de entrada inválido."`

### test_agregar_bebida_invalida_nombre

Este caso de prueba verifica que una entrada con un nombre de artículo no válido no se agregue al sistema.

Entrada: `"T,12,16,20"`

Resultado esperado: `"Error: El nombre del artículo debe contener caracteres alfabéticos y tener una longitud de 2 a 15 caracteres."`

### test_agregar_bebida_invalida_tamano

Este caso de prueba verifica que una entrada con tamaños no válidos no se agregue al sistema.

Entrada: `"Mocha,0,12,16"`

Resultado esperado: `"Error: Los tamaños deben ser valores enteros dentro del rango de 1 a 48 y deben estar en orden ascendente."`

### test_agregar_bebida_duplicada

Este caso de prueba verifica que no se agregue una bebida duplicada al sistema.

Entrada: `"Latte,12,16,20"` (Agregando la misma bebida dos veces)

Resultado esperado: `"Error: El nombre del artículo ya existe en el sistema."`