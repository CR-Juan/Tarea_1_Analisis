"""
=========================================
           Funciones de Busqueda
=========================================
"""
def BusquedaBinaria_matriz(matriz, objetivo):
    for fila in matriz:
        if BusquedaBinaria(fila, objetivo):
            return True
    return False

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

def busqueda_matriz(matriz, objetivo):
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