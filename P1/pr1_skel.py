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
    ...

def multiplica_escalar(matriz, k):
    ...

def suma(matriz1, matriz2):
    ...


# Ejercicio 2
def validar(grafo):
    ...

def grado_entrada(grafo, nodo):
    ...

def distancia(grafo, nodo):
    ...
   
