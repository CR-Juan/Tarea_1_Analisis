import random # Libreria para generar listas con numeros randoms.
import time # Libreria para visaulizar el tiempo de ejecución del programa.
import tracemalloc # Libreria para visualizar la cantidad de memoria que utiliza la ejecucion del programa.
from algoritmo_ordenamiento import quicksort # Importa la función de ordenamiento creada por el grupo.


"""
============================================
           Funciones de Busqueda
============================================
"""

# Función de busqueda por medio de Busqueda Binaria (Función reutilizada para comparar Búsqueda Binaria vs función generada por el grupo).
def BusquedaBinaria(lista, objetivo):
    if not isinstance(lista,list):
        print("El argumento 'lista' debe ser una lista.")
        return False
    
    izq = 0 # Índice inicial.
    derecha = len(lista) - 1 # Índice final.
    # Validar que no se crucen los límites izquierda y derecha.
    while izq <= derecha:
        mitad = izq + (derecha - izq) // 2 # Elemento central de la lista.
        if (lista[mitad] == objetivo): # Ver si el elemento del medio es igual al elemento que estamos buscando.
            return True
        elif (lista[mitad] < objetivo): # Si el elemento es mayor a la mitad, buscamos en la parte derecha.
            izq = mitad + 1
        else:
            derecha = mitad - 1 # Si el elemento es menor a la mitad, buscamos en la parte izquierda.
    return False

# Función que recorre cada una de las listas de la matriz y aplica la busqueda binaria.
def BusquedaBinaria_matriz(matriz, objetivo):
    if not isinstance(matriz, list):
        print("El argumento 'matriz' debe ser una lista.")
        return False
    for fila in matriz:
        if BusquedaBinaria(fila, objetivo):
            return True
    return False

# Función que recorre cada una de las listas de la matriz y aplica la función de busqueda realizada por el grupo.
def busqueda_matriz(matriz, objetivo):
    if not isinstance(matriz, list):
        print("El argumento 'matriz' debe ser una lista.")
        return False
    
    for lista in matriz:
        if busqueda_grupal(lista, objetivo):
            return True
    return False

# Función de busqueda creada por el grupo.
def busqueda_grupal(lista, objetivo):
    if not isinstance(lista,list):
        print("El argumento 'lista' debe ser una lista.")
        return False
    # Valida que la lista no esté vacía.
    if lista == []:
        return False
    mitad = len(lista) // 2 # Saca el índice central de la lista.
    izq = lista[:mitad] # Variable que almacena la lista de elementos del índice inicial a la derecha.
    derecha = lista[mitad:] # Variable que almacena la lista de los elementos desde el inicio de la lista hasta el índice central.
    # Mientras que ninguno de los extremos de la lista sea vacío se ejecuta.
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

def crear_matriz(filas,columnas):
    matriz = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila.append(random.randint(1, 100))
        matriz.append(fila)
    return matriz

def prueba_rendimiento(filas,columnas):
    # Prueba de rendimiento para la función de búsqueda binaria.
    inicio = time.time()
    tracemalloc.start()

    matriz = crear_matriz(filas,columnas)
    num_busqueda = matriz[random.randint(0, filas-1)][random.randint(0, columnas-1)]
    matriz2 = quicksort(matriz)
 
    BusquedaBinaria_matriz(matriz2, num_busqueda)

    fin = time.time()
    memoria = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"\nTiempo de ejecución (Búsqueda Binaria): {fin - inicio} segundos")
    print(f"Uso de memoria (Búsqueda Binaria): {memoria[1] / 10**6} MB\n")

    # Prueba de rendimiento para la función de búsqueda custom.
    inicio = time.time()
    tracemalloc.start()

    matriz = crear_matriz(filas,columnas)
    num_busqueda = matriz[random.randint(0, filas-1)][random.randint(0, columnas-1)]
    matriz2 = quicksort(matriz)

    busqueda_grupal(matriz, num_busqueda)

    fin = time.time()
    memoria = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Tiempo de ejecución (Búsqueda Grupal): {fin - inicio} segundos")
    print(f"Uso de memoria (Búsqueda Grupal): {memoria[1] / 10**6} MB")

prueba_rendimiento(100,100)