import random # Libreria para generar listas con numeros randoms.
import time # Libreria para visaulizar el tiempo de ejecución del programa.
import tracemalloc # Libreria para visualizar la cantidad de memoria que utiliza la ejecucion del programa.

"""
=========================================
        Funciones de Ordenamiento
=========================================
"""

# Función para sumar listas (opcional).
def suma_Lista(Lista):
    suma = 0
    New_Lista = []
    for x in Lista:
        suma += x
    New_Lista += [suma]
    return New_Lista

# Función para ordenar las listas de la matriz.
def ordenar_Listas_enMatriz(Matriz):
    for _ in range(len(Matriz)):
        for x in range(len(Matriz)-1):
            if Matriz[x][0] > Matriz[x + 1][0]:
                Matriz[x], Matriz[x + 1] = Matriz[x + 1], Matriz[x]
    return Matriz 

# Función que genera números aleatorios para posteriormente agregarlos a las listas de la matriz.
def Numero_aleatorio():
    return random.randint(-100000, 100000)

# Función de ordenamiento Quicksort (Función reutilizada para probar función Quicksort vs función generada por el grupo).
def quicksort(arr):
    # Caso inicial donde las listas pueden estar vacías o si la lista posee un solo elemento.
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[len(arr) // 2]  # Se selecciona el elemento central de la lista para utilizarlo como pivote.
        izquierda = [x for x in arr if x < pivote]
        centro = [x for x in arr if x == pivote]
        derecha = [x for x in arr if x > pivote]
        return quicksort(izquierda) + centro + quicksort(derecha)

# Función para ordenar cada una de las listas que están dentro de la matriz.
def ordenar_MatrizAleatoria(Matriz):
    for x in range(len(Matriz)):
        Matriz[x] = suma_Lista(Matriz[x]) # En caso de comprobar la funcionalidad del programa con "Quicksort" cambiar esta linea por lo siguiente: Matriz[x] = quicksort(Matriz[x])
    Matriz = ordenar_Listas_enMatriz(Matriz)
    return Matriz

                
# Función para crear una matriz con la cantidad de filas y columnas recibidas y ordenarla para mostrarla.
def Crear_Matriz(filas, columnas):
    if not isinstance(filas,int) or not isinstance(columnas,int):
        return "Los datos deben de ser enteros"
    elif filas < 1 or columnas < 1:
        return "Los datos deben de ser mayor a 0"
    else:
        inicio = time.time() # Se inicia el tiempo de ejecución del programa.
        tracemalloc.start() # Se inicia el control de memoria durante la ejecución del programa.
        matriz = []
        for _ in range(filas):
            fila = []
            for _ in range(columnas):
                fila += [Numero_aleatorio()] # Fila se rellena con números aleatorios.
            matriz += [fila]
        matriz = ordenar_MatrizAleatoria(matriz)
        final = time.time() # Se finaliza el tiempo de ejecución del programa.
        Duracion = final - inicio # Se resta el tiempo inicial del tiempo final para calcular el tiempo total.
        Actual, Maximo = tracemalloc.get_traced_memory() # Variables para almacenar la memoria actual y el pico máximo de la memoria utilizada.
        tracemalloc.stop() # Se frena el control de memoria de la ejecución del programa.
        # Se muestra el tiempo de la ejecición, la memoria actual, la memoria máxima utilizada y la matriz ordenada.
        return (
                f"Duracion: {Duracion}\n"
                f"Memoria Actual: {Actual}\n"
                f"Memoria Pico: {Maximo}\n"
                f"Matriz: {matriz}\n"
                )

#print(Crear_Matriz(3,3))