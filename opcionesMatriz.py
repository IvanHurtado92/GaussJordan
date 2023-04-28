import numpy as np
from fractions import Fraction

def crearMat(n):
    arr = np.zeros((n,(n+1)))
    for i in range(n):
        for j in range(n+1):
            arr[i][j] = int(input(f'Ingresa el valor del indice [{i+1}],[{j+1}] ---> '))
        print()
    print(f'\nArreglo original\n\n{arr}')
    return arr;

def reducir(arr,n):
    arr2 = np.zeros((n,(n+1)))
    for r in range(n):
        for i in range(n):
            if (i==r): continue

            for j in range(n+1):
                arr2[i][j] = arr[i][j] - ((arr[i][r] / arr[r][r]) * arr[r][j])
        for i in range(n):
            if (i==r): continue

            for j in range(n+1):
                arr[i][j] = arr2[i][j]
        
    print(f'\nArreglo Escalonado\n\n{arr}')
    arr3 = simplificar(arr,n)
    resultados(arr3,n)
    return arr3

def simplificar(arr,n):
    arr2 = np.zeros((n,(n+1)))
    arr3 = []
    for i in range(n):
        subarr = []
        for j in range(n+1):
            arr2[i][j] = arr[i][j] * (1/arr[i][i])
            subarr.append(str(Fraction(arr2[i][j]).limit_denominator()))
        arr3.append(subarr)
    
    print(f'\nArreglo simplificado\n')
    for i in range(n):
        print(arr3[i])
    return arr3

def resultados(arr,n):
    for i in range(n):
        print(f'x{i} = {arr[i][n]}')
