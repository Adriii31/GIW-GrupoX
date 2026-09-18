"""
Asignatura: GIW
Práctica 1
Grupo: 10
Autores: Miguel Sevilla Benito, Izan de Vega López

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
    if len(matriz) == 0 or matriz is None:
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
    
    # Will check:
    # - a b d
    # a - c e
    # b c - f
    # d e f -
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
    if((dimension is None) or (k is None)):
        return None

    return_value = copy.deepcopy(matriz)
    for y_idx in range(len(return_value)):
        for x_idx in range(len(return_value[y_idx])):
            return_value[y_idx][x_idx] *= k

    return return_value


def suma(matriz1, matriz2):
    d1 = dimension(matriz1)
    d2 = dimension(matriz2)

    # Comprobar que las matrices están bien formadas
    # y tienen la misma dimensión
    if d1 is None or d2 is None or d1 != d2:
        return None

    matriz3 = []

    for i in range(len(matriz1)):
        fila = []

        for j in range(len(matriz1[i])):
            resultado = matriz1[i][j] + matriz2[i][j]
            fila.append(resultado)

        matriz3.append(fila)

    return matriz3
        


# Ejercicio 2
def validar(grafo):
    ...

def grado_entrada(grafo, nodo):
    ...

def distancia(grafo, nodo):
    ...
   


if __name__ == "__main__":
    print("--- EJERCICIO 1 ---")
    matriz_normal = [[1, 2, 3], [4, 5, 6]]
    matriz_cuadrada = [[1, 2], [3, 4]]
    matriz_mal_formada = [[1, 2], [3, 4, 5]]
    matriz_no_simetrica = [[1, 1, 3], [2,2,3], [3,3,3]]
    matriz_simetrica = [[1, 2, 3], [2,5,2], [3,2,3]]
    
    # Funciones implementadas
    print(f"Dimensión matriz_normal: {dimension(matriz_normal)}")            # (2, 3)
    print(f"Dimensión matriz_mal_formada: {dimension(matriz_mal_formada)}")  # None
    print(f"Es cuadrada matriz_cuadrada: {es_cuadrada(matriz_cuadrada)}")    # True
    print(f"Es cuadrada matriz_normal: {es_cuadrada(matriz_normal)}")        # False

    print(f"Es simetrica matriz_simetrica: {es_simetrica(matriz_simetrica)}") # True
    print(f"Es simetrica matriz_no_simetrica: {es_simetrica(matriz_no_simetrica)}") # False
    print(f"Es simetrica matriz_normal: {es_simetrica(matriz_normal)}") # False

    print(f"Suma matriz_normal + matriz_normal: {suma(matriz_normal,matriz_normal)}") # Same as below
    print(f"Multiplicación 2* matriz_normal: {multiplica_escalar(matriz_normal,2)}") # Same as above

    print(f"Es simétrica: {es_simetrica(matriz_simetrica)}")
    print(f"Multiplica escalar x2: {multiplica_escalar(matriz_normal, 2)}")
