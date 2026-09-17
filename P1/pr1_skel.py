"""
TODO: rellenar

Asignatura: GIW
Práctica 1
Grupo: XXXXXXX
Autores: XXXXXX 

Declaramos que esta solución es fruto exclusivamente de nuestro trabajo personal. No hemos
sido ayudados por ninguna otra persona o sistema automático ni hemos obtenido la solución
de fuentes externas, y tampoco hemos compartido nuestra solución con otras personas
de manera directa o indirecta. Declaramos además que no hemos realizado de manera
deshonesta ninguna otra actividad que pueda mejorar nuestros resultados ni perjudicar los
resultados de los demás.
"""

import copy

# Ejercicio 1

#devuelve una tuple (filas, columnas) con el tamaño de la matriz. Si la matriz esta mal formada
#debera devolver none
def dimension(matriz):
    if len(matriz) == 0:
        return None
    filas = len(matriz)
    columnas = len(matriz[0])
    
    for fila in matriz:
        if len(fila) != columnas:
            return None
    
    return (filas, columnas)

def es_cuadrada(matriz):
    tamanio = dimension(matriz)

    if tamanio == None:
        return False
    filas = tamanio[0]
    columnas = tamanio[1]
    
    if filas == columnas:
        return True
    else:
        return False

def es_simetrica(matriz):
    if(not es_cuadrada(matriz)):
        return False
    
    # Comprobamos que todos los elementos en el lado inferior izquierdo de la división producida por la diagonal coinciden con aquellos en su posición simétrica en función de dicha diagonal
    y = 1
    while(y < len(matriz)):
        x = 0
        while(x < y):
            if(matriz[x][y] != matriz[y][x]):
                return False
            x += 1
        y += 1

    return True


def multiplica_escalar(matriz, k):
    if(dimension is None):
        return None

    return_value = copy.deepcopy(matriz)
    for y_idx in range(len(return_value)):
        for x_idx in range(len(return_value[y_idx])):
            return_value[y_idx][x_idx] *= k

    return return_value


def suma(matriz1, matriz2):
    ...


# Ejercicio 2
def validar(grafo):
    ...

def grado_entrada(grafo, nodo):
    ...

def distancia(grafo, nodo):
    ...
   

if __name__ == "__main__":
    matriz = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print(matriz)
    print(dimension(matriz))
    print(es_cuadrada(matriz))
    print(es_simetrica(matriz))
    print(multiplica_escalar(matriz,2))
    print(matriz)