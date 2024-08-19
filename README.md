# Kata:

## Introducción

Para esta kata, se utilizó un hash MD5 para obtener un número entre 1 y 9. Al ingresar el nombre "Julian Sanchez", el número seleccionado es 1. Esta prueba fue realizada en Python.


## code_one.py : Filtrado e Inversión de Números

Este código realiza las siguientes funciones:

### 1. Filtrado de Números (`filter_numbers`)

- **Descripción:** Esta función filtra los números eliminando los dígitos que son mayores o iguales a un umbral especificado por el usuario.
- **Entrada:** 
  - Una lista de números.
  - Un umbral (número) para el filtrado.
- **Salida:** 
  - Una lista de números filtrados que cumplen con la condición.

### 2. Inversión de Números (`reverse_numbers`)

- **Descripción:** Esta función invierte el orden de los elementos en una lista.
- **Entrada:** 
  - Una lista de números.
- **Salida:** 
  - La misma lista pero en orden inverso.

### 3. Generación de Lista Aleatoria (`generate_random_list`)

- **Descripción:** Esta función genera una lista de números aleatorios.
- **Entrada:** 
  - El tamaño de la lista que se desea generar.
- **Salida:** 
  - Una lista de números aleatorios.

### 4. Función Principal (`main`)

- **Descripción:** Esta es la función principal del programa que presenta un menú al usuario para ingresar una lista manualmente o generar una lista aleatoria. Luego, solicita un umbral para filtrar los números, aplica el filtrado, invierte la lista filtrada, y finalmente muestra la lista resultante.
- **Flujo del Programa:**
  1. El usuario elige entre ingresar una lista manualmente o generar una lista aleatoria.
  2. Se solicita un umbral para el filtrado de los números.
  3. Los números se filtran según el umbral y la lista resultante se invierte.
  4. Se muestra la lista filtrada e invertida al usuario.

## Ejecución del Código

Para ejecutar este código, simplemente corre el archivo `code_one.py`. El programa te guiará a través de las opciones para ingresar o generar una lista, y luego aplicará las funciones de filtrado e inversión para mostrarte el resultado final.


```bash
py code_one.py
```

## code_two.py : Cuadrados Ordenados con Filtrado

Este código realiza las siguientes funciones:

### 1. Ordenar y Filtrar Cuadrados (`sorted_squares`)

- **Descripción:** Esta función toma una lista de enteros ordenados en orden ascendente y devuelve una nueva lista con los cuadrados de los enteros originales, también ordenados en orden ascendente. Si el número cuadrado está fuera del rango `[0, threshold]`, se elimina de la lista de salida.
- **Entrada:**
  - Una lista de enteros ordenados en orden ascendente.
  - Un umbral (número) para el rango de salida.
- **Salida:**
  - Una lista de cuadrados ordenados en orden ascendente dentro del rango permitido.

### 2. Ordenamiento con Counting Sort (`counting_sort`)

- **Descripción:** Esta función ordena una lista de enteros en orden ascendente utilizando el algoritmo Counting Sort.
- **Entrada:**
  - Una lista de enteros a ordenar.
  - Un umbral (número) para el rango de salida.
- **Salida:**
  - Una lista de enteros ordenados en orden ascendente.

### 3. Generación de Lista Aleatoria (`generate_random_list`)

- **Descripción:** Esta función genera una lista aleatoria de enteros.
- **Entrada:**
  - El tamaño de la lista que se desea generar.
  - El valor mínimo y máximo de los enteros en la lista.
- **Salida:**
  - Una lista de enteros aleatorios.

### 4. Función Principal (`main`)

- **Descripción:** Esta es la función principal del programa que presenta un menú al usuario para ingresar una lista manualmente o generar una lista aleatoria. Luego, solicita un umbral, calcula los cuadrados, aplica el filtrado, ordena la lista resultante, y finalmente muestra la lista.
- **Flujo del Programa:**
  1. El usuario elige entre ingresar una lista manualmente o generar una lista aleatoria.
  2. Se solicita un umbral para el rango de salida.
  3. Se calculan los cuadrados de los números en la lista, se filtran y ordenan.
  4. Se muestra la lista de cuadrados ordenados dentro del rango permitido.

## Ejecución del Código

Para ejecutar este código, simplemente corre el archivo `code_two.py`. El programa te guiará a través de las opciones para ingresar o generar una lista, aplicar las funciones de ordenamiento y filtrado, y finalmente mostrarte el resultado.

```bash
py code_two.py
```

## code_two_v2.py : Mejora en Cuadrados Ordenados con Filtrado

Este código es una versión mejorada del `code_two.py` y presenta las siguientes mejoras:

### 1. Optimización en el Ordenamiento de Cuadrados (`sorted_squares`)

- **Descripción:** Esta función optimiza el cálculo y ordenamiento de los cuadrados de una lista de enteros ordenados. Utiliza un enfoque de dos punteros para calcular y ordenar los cuadrados de manera más eficiente.
- **Entrada:**
  - Una lista de enteros ordenados en orden ascendente.
  - Un umbral (número) para el rango de salida.
- **Salida:**
  - Una lista de cuadrados ordenados en orden ascendente dentro del rango permitido.

- **Mejoras respecto a `code_two.py`:**
  - **Eficiencia:** La nueva implementación usa un enfoque de dos punteros para comparar los cuadrados de los números en los extremos de la lista, lo que mejora la eficiencia en comparación con el método de Counting Sort.
  - **Complejidad:** Reducción en la complejidad de tiempo al evitar la necesidad de una lista de conteo y al ordenar directamente los cuadrados filtrados.

### 2. Generación de Lista Aleatoria (`generate_random_list`)

- **Descripción:** Esta función sigue generando una lista aleatoria de enteros, sin cambios respecto a la versión anterior.
- **Entrada:**
  - El tamaño de la lista que se desea generar.
  - El valor mínimo y máximo de los enteros en la lista.
- **Salida:**
  - Una lista de enteros aleatorios.

### 3. Función Principal (`main`)

- **Descripción:** Esta función principal presenta un menú al usuario para ingresar una lista manualmente o generar una lista aleatoria. Luego solicita un umbral, calcula los cuadrados, aplica el filtrado, y muestra la lista resultante.
- **Flujo del Programa:**
  1. El usuario elige entre ingresar una lista manualmente o generar una lista aleatoria.
  2. Se solicita un umbral para el rango de salida.
  3. Se calculan los cuadrados de los números en la lista, se filtran y ordenan utilizando el nuevo enfoque optimizado.
  4. Se muestra la lista de cuadrados ordenados dentro del rango permitido.

## Ejecución del Código

Para ejecutar este código, simplemente corre el archivo `code_two_v2.py`. El programa te guiará a través de las opciones para ingresar o generar una lista, aplicar las funciones de ordenamiento y filtrado mejoradas, y finalmente mostrarte el resultado.

```bash
py code_two_v2.py
```

## Aclaración sobre el Umbral

En ambos códigos (`code_two.py` y `code_two_v2.py`), el umbral solo necesita ser ingresado una vez. No es necesario duplicar el umbral en la entrada.


## code_three.py : Cambio Mínimo Imposible

Este código realiza las siguientes funciones:

### 1. Cálculo del Cambio Mínimo Imposible (`minimum_change`)

- **Descripción:** Dada una lista de enteros positivos que representan los valores de las monedas en tu posesión, esta función devuelve la cantidad mínima de cambio (la suma mínima de dinero) que no puedes dar como cambio. Esto se basa en el concepto de que si tienes una serie de monedas ordenadas, la cantidad mínima que no puedes representar es el primer valor que no puedes formar usando las monedas disponibles hasta ese punto.
- **Entrada:** 
  - Una lista de enteros positivos que representan los valores de las monedas.
- **Salida:** 
  - Un entero que representa la cantidad mínima de cambio que no se puede crear.

### 2. Generación de Lista Aleatoria (`generate_random_list`)

- **Descripción:** Esta función genera una lista aleatoria de enteros positivos.
- **Entrada:** 
  - El tamaño de la lista que se desea generar.
  - El valor máximo de los enteros en la lista.
- **Salida:** 
  - Una lista de enteros aleatorios generados entre 1 y el valor máximo especificado.

### 3. Función Principal (`main`)

- **Descripción:** Esta función presenta un menú al usuario para ingresar una lista manualmente o generar una lista aleatoria. Luego, calcula el cambio mínimo imposible usando la función `minimum_change` y muestra el resultado.
- **Flujo del Programa:**
  1. El usuario elige entre ingresar una lista manualmente o generar una lista aleatoria.
  2. Si se ingresa una lista manualmente, se solicita al usuario los valores de las monedas separados por comas.
  3. Si se elige generar una lista aleatoria, se solicita el tamaño de la lista y el valor máximo de los enteros.
  4. Se calcula el cambio mínimo imposible y se muestra al usuario.

## Ejecución del Código

Para ejecutar este código, simplemente corre el archivo `code_three.py`. El programa te guiará a través de las opciones para ingresar o generar una lista de monedas, y luego calculará y mostrará la cantidad mínima de cambio que no puedes dar como cambio.

```bash
py code_three.py
```