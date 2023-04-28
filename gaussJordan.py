"""
Programación científica
Carlos Leonardo Cruz Ortiz
Ivan Israel Hurtado Lozano
Gauss Jordan

El método de Gauss-Jordan es un algoritmo que se usa para determinar la inversa de una matriz y
las soluciones de un sistema de ecuaciones lineales.

Un sistema de ecuaciones se resuelve por el método de Gauss cuando se obtienen sus soluciones 
mediante la reducción del sistema dado a otro equivalente en el que cada ecuación tiene una 
incógnita menos que la anterior. El método de Gauss transforma la matriz de coeficientes en 
una matriz triangular superior. El método de Gauss-Jordan continúa el proceso de transformación
hasta obtener una matriz diagonal. 

Ultima actualización: 4 de abril del 2023
"""

import opcionesMatriz,os

os.system('cls')

incog = int(input('Ingresa el numero de incognitas en el sistema ---> '))
print()

arr = opcionesMatriz.crearMat(incog)


arr2 = opcionesMatriz.reducir(arr,incog)
