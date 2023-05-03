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
    tipo=1 #tipo es el tipo de respuesta que es, resolvible, infinita o sin solucion (1,2,3)
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
        
        #Esta zona nos permite eliminar valores hasta que la línea debajo de la actual no exprese que los resultados son infinitos o sin solución

        terminado = False # revisa si ya se llegó el penultimo elemento de la fila para el caso de ceros1
        ceros1 = True # cuenta todos los numeros de la fila excepto el ultimo
        ceros2 = False # cuenta todos los numeros de la fila

        for k in range(n): #buscando los elementos de la fila debajo de la actual excepto el último, busca si es sin solución(todos los elementos menos el último es igual a cero)
            if(r+1==n):break # si se pasó de la cantidad de filas existentes, se rompe el ciclo
            if(k == n-1):terminado=True # si ya se llegó al penúltimo elmento
            if(arr[r+1][k]!=0):ceros1=False # revisa si todos los numeros de la fila excepto el ultimo son ceros
            # print(terminado)

            if(ceros1 and terminado): 
                ceros2 = True
                for g in range(n+1): #buscando todos los elementos de la fila debajo de la actual, busca si tiene soluciones infinitas (todos son ceros en la fila)
                    if(arr[r+1][g]!=0):ceros2=False # revisa si todos los numeros de la fila son ceros
        # print(ceros1,ceros2)
        if(ceros2):
            tipo = 2 #soluciones infinitas
            break
        elif(ceros1 and arr[n-1][n]!=0):
            tipo = 3 #sin solución
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
