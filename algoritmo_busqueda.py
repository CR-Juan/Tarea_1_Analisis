"""
============================================
           Funciones de Busqueda
============================================
"""

# Función de busqueda por medio de Busqueda Binaria (Función reutilizada para comparar Búsqueda Binaria vs función generada por el grupo).
def BusquedaBinaria(lista, objetivo):
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
    for fila in matriz:
        if BusquedaBinaria(fila, objetivo):
            return True
    return False

# Función que recorre cada una de las listas de la matriz y aplica la función de busqueda realizada por el grupo.
def busqueda_matriz(matriz, objetivo):
    for lista in matriz:
        if busqueda_grupal(lista, objetivo):
            return True
    return False

# Función de busqueda creada por el grupo.
def busqueda_grupal(lista, objetivo):
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