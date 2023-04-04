import numpy as np

def crearMat(n):
    arr = np.zeros((n,(n+1)))
    for i in range(n):
        for j in range(n+1):
            arr[i][j] = int(input(f'Ingresa el valor del indice [{i+1}],[{j+1}] ---> '))
    print(arr)
    return arr;


