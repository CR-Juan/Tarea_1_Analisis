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

"""""
=========================================
            Funciones de prueba
=========================================
"""
def Numero_aleatorio():
    return random.randint(100, 100000)
def Crear_Matriz_2(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila += [Numero_aleatorio()]
        matriz += [fila]
    
    return matriz

"""

=========================================
           Funciones de Busqueda
=========================================
"""
def BusquedaBinaria(lista, objetivo):
    izq = 0
    derecha = len(lista) - 1
    while izq <= derecha:
        mitad = izq + (derecha - izq) // 2
        if (lista[mitad] == objetivo):
            return True
        elif (lista[mitad] < objetivo):
            izq = mitad + 1
        else:
            derecha = mitad - 1
    return False

def BusquedaBinaria_matriz(matriz, objetivo):
    for fila in matriz:
        if BusquedaBinaria(fila, objetivo):
            return True
    return False

def busqueda_matriz(matriz, objetivo): #n
    for lista in matriz:
        if busqueda_matriz_rec(lista, objetivo):
            return True
    return False

def busqueda_matriz_rec(lista, objetivo):
    if lista == []:
        return False
    
    mitad = len(lista) // 2
    izq = lista[:mitad]
    derecha = lista[mitad:]

    while (izq != [] or derecha != []):
        if izq != []:
            if izq[0] == objetivo:
                return True
            izq = izq[1:]

        if derecha != []:
            if derecha[0] == objetivo:
                return True
            derecha = derecha[1:]
        
    return False
