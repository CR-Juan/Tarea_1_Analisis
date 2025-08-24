import random
import time
import tracemalloc

def Numero_aleatorio():
    return random.randint(100, 100000)

def quicksort(arr):
    # Caso base: listas vacías o de un solo elemento ya están ordenadas
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[len(arr) // 2]  # elijo el elemento del medio como pivote
        izquierda = [x for x in arr if x < pivote]
        centro = [x for x in arr if x == pivote]
        derecha = [x for x in arr if x > pivote]
        return quicksort(izquierda) + centro + quicksort(derecha)



def ordenar_MatrizAleatoria(Matriz):
    for x in range(len(Matriz)):
        Matriz[x] = ordenar_listaMatriz(Matriz[x])
    return Matriz

def ordenar_listaMatriz(lista):
    NewLista = []
    while lista != []:
        x = lista[0]
        lista = lista[1:]
        y = 0
        while y < len(lista):
            if x > lista[0]:
                lista += [x]
                x = lista[0]
                lista = lista[1:]
                y += 1
            else:
                lista += [lista[0]]
                lista = lista[1:]
                y += 1
                
        NewLista += [x]
    return NewLista
                
def Crear_Matriz(filas, columnas):
    inicio = time.time()
    tracemalloc.start()
    matriz = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila += [Numero_aleatorio()]
        matriz += [fila]
    final = time.time()
    Duracion = final - inicio
    Actual, Maximo = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return (
            f"Duracion: {Duracion}\n"
            f"Memoria Actual: {Actual}\n"
            f"Memoria Pico: {Maximo}\n"
            f"Matriz: {ordenar_MatrizAleatoria(matriz)}\n"
             )   
       
print(Crear_Matriz(10,10))

"""
Quicksort:
Duracion: 1.3334903717041016
Memoria Actual: 10099512
Memoria Pico: 10099708

Mio:
Duracion: 0.9638333320617676
Memoria Actual: 10098968
Memoria Pico: 10099164
"""


