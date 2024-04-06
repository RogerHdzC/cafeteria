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
└── main.py  # Script para probar de manera manual el programa

```

## Funcionalidades

El módulo `cafeteria.py` proporciona las siguientes funcionalidades:

- `Cafeteria`: Clase principal que gestiona las bebidas en la cafetería.
- `agregar_bebida(entrada)`: Método para agregar nuevas bebidas al sistema, con validación del formato de entrada.

## Ejecución de Pruebas

Para ejecutar las pruebas, asegúrese de tener instalado pytest y luego ejecute el siguiente comando en la raíz del proyecto:

```
pip install -r requirements.txt

pytest
```

## Descripción de Casos de Prueba

El programa y los casos de prueba proporcionados cumplen con las especificaciones y criterios de aceptación indicados. Aquí está la evaluación de cómo cada aspecto de las especificaciones y criterios de aceptación se aborda en el código y las pruebas:

### Especificaciones de entrada:
1. El nombre de la bebida debe contener caracteres alfabéticos y tener una longitud de 2 a 15 caracteres.
   - Se verifica que el nombre del artículo sea alfabético y tenga una longitud adecuada en la función `agregar_bebida` del programa y en las pruebas correspondientes (`test_agregar_bebida_nombre_valido`, `test_agregar_bebida_nombre_invalido_longitud_minima`, `test_agregar_bebida_nombre_invalido_longitud_maxima`, `test_agregar_bebida_formato_invalido_nombre_numerico`).
  
2. El tamaño de la bebida puede variar, permitiendo un máximo de cinco tamaños por artículo, y debe ser un valor entero dentro del rango de 1 a 48.
   - Se verifica que los tamaños estén dentro del rango adecuado y sean enteros en la función `agregar_bebida` del programa y en las pruebas correspondientes (`test_agregar_bebida_tamano_valido`, `test_agregar_bebida_tamano_invalido_valor_fuera_de_rango`, `test_agregar_bebida_tamano_invalido_no_entero`, `test_agregar_bebida_formato_invalido_tamano_letras`, `test_agregar_bebida_formato_invalido_tamano_vacios`, `test_agregar_bebida_formato_invalido_tamano_demasiados_ceros`, `test_agregar_bebida_formato_invalido_tamano_negativo`, `test_agregar_bebida_formato_invalido_tamano_decimal`).
   
3. Los tamaños deben ingresarse en orden ascendente (los más pequeños primero).
   - Se verifica que los tamaños estén en orden ascendente en la función `agregar_bebida` del programa y en las pruebas correspondientes (`test_agregar_bebida_tamano_invalido_no_orden_ascendente`).
   
4. El nombre del artículo se debe ingresar primero, seguido de una coma y luego una lista de tamaños.
   - Se verifica el formato de entrada en la función `agregar_bebida` del programa y en las pruebas correspondientes (`test_agregar_bebida_formato_invalido_falta_coma`, `test_agregar_bebida_formato_invalido_sobran_comas`).
   
5. Una coma separará cada tamaño.
   - Se verifica el formato de entrada en la función `agregar_bebida` del programa y en las pruebas correspondientes (`test_agregar_bebida_formato_invalido_falta_coma`, `test_agregar_bebida_formato_invalido_sobran_comas`).
   
6. Se ignorarán los espacios en blanco en cualquier lugar de la entrada.
   - Se eliminan los espacios en blanco de la entrada en la función `agregar_bebida` del programa.

### Criterios de aceptación:
1. El nombre del artículo es alfabético (válido)
   - Verificado en las pruebas.

2. El nombre del artículo tiene menos de 2 caracteres de longitud (inválido)
   - Verificado en las pruebas.

3. El nombre del artículo tiene de 2 a 15 caracteres de longitud (válido)
   - Verificado en las pruebas.

4. El valor del tamaño está en el rango de 1 a 48 (válido)
   - Verificado en las pruebas.

5. El valor del tamaño es un número entero (válido)
   - Verificado en las pruebas.

6. Los valores del tamaño se ingresan en orden ascendente (válido)
   - Verificado en las pruebas.

7. Se ingresan de uno a cinco valores de tamaño (válido)
   - Verificado en las pruebas.

8. El nombre del artículo es el primero en la entrada (válido)
   - Verificado en las pruebas.

9. Una sola coma separa cada entrada en la lista (válido)
   - Verificado en las pruebas.

10. La entrada contiene o no espacios en blanco (a especificar en las pruebas)
    - Verificado en las pruebas.

### Evaluación general:
El código y las pruebas proporcionadas abordan adecuadamente todas las especificaciones y criterios de aceptación. Los casos de prueba cubren tanto los casos válidos como los casos inválidos, y se verifica el comportamiento esperado del programa en cada uno de ellos. 