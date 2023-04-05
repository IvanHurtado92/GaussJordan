import opcionesMatriz,os;

os.system('cls')

incog = int(input('Ingresa el numero de incognitas en el sistema ---> '))

arr = opcionesMatriz.crearMat(incog);


arr2 = opcionesMatriz.reducir(arr,incog)
