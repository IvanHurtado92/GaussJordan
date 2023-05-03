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
    tipo=1 #tipo es el tipo de respuesta que es, resolvible, sin solucion o infinita
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

        print(f'\nArreglo {r}\n\n{arr}')
        
        suma = 0
        suma2 = 0
        encontrado = False

        for k in range(n): #sumando los elementos de la fila debajo de la actual excepto el último
            if(r+1==n):break
            suma2+=arr[r+1][k]
            if(suma2==0):
                for k in range(n+1): #sumando todos los elementos de la fila debajo de la actual
                    if(r+1==n):break
                    suma+=arr[r+1][k]



        # for k in range(n+1): #sumando los elementos de la ultima fila
        #     suma+=arr[n-1][k]

        # for k in range(n): #sumando los elementos de la ultima fila excepto el último
        #     suma2+=arr[n-1][k]

        if(suma==0):
            tipo = 2
            break
        elif(suma2 == 0 and arr[n-1][n]!=0):
            tipo = 3
            break

    print(f'\nArreglo Escalonado\n\n{arr}')
    arr3 = simplificar(arr,n,tipo)
    resultados(arr3,n,tipo)
    return arr3

def simplificar(arr,n,tipo):
    arr2 = np.zeros((n,(n+1)))
    arr3 = []

    if(tipo == 1):
        for i in range(n):
            subarr = []
            for j in range(n+1):
                arr2[i][j] = arr[i][j] * (1/arr[i][i])
                subarr.append(str(Fraction(arr2[i][j]).limit_denominator()))
            arr3.append(subarr)
    
    elif(tipo==2):
        for i in range(n-1):
            subarr = []
            for j in range(n+1):
                arr2[i][j] = arr[i][j] * (1/arr[i][i])
                subarr.append(str(Fraction(arr2[i][j]).limit_denominator()))
            arr3.append(subarr)
        subarr = []
        for k in range(n+1):
            subarr.append(str(Fraction(arr2[n-1][k]).limit_denominator()))
        arr3.append(subarr)
    
    if(tipo!=3):
        print(f'\nArreglo simplificado\n')
        for i in range(n):
            print(arr3[i])
    return arr3

def resultados(arr,n,tipo):
    if(tipo==1):
        for i in range(n):
            print(f'x{i} = {arr[i][n]}')
    elif(tipo==2):
        print('\nSoluciones infinitas\n')

        for i in range(n):
            for j in range(n+1):
                arr[i][j] = Fraction(arr[i][j])

        for i in range(n-1):
            txt = ''
            if((float(arr[i][n-1]))>0):
                txt='-'
                print(f'x{i} = {arr[i][n]} {txt} {arr[i][n-1]} x{n-1}')
            else:
                txt='+'
                print(f'x{i} = {arr[i][n]} {txt} {-arr[i][n-1]} x{n-1}')
        print(f'x{n-1}')
    else:
        print('\nEl sistema no tiene solución!!\n')
