'''
Escribir una función que, dado un número entero 𝑛, permita calcular su factorial.

'''
#ejemplo factoria de 5; 5! = 5 X 4 X 3 X 2 X 1 = 120

def factorial(n):
    resultado = 1
    for i in range (1, (n+1)):
        resultado*= i

    return resultado 


