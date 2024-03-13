'''Escribir funciones que resuelvan los siguientes problemas:
a) Dados dos números, imprimir la suma, resta, división y multiplicación de ambos.
b) Dado un número natural 𝑛, imprimir su tabla de multiplicar.'''

#a)
def operaciones_fundamentales(n1,n2):
    resultado = n1+n2
    print("La suma es", resultado)
    resultado = n2-n1 
    print("La resta es", resultado)
    resultado = n2/n1 
    print("La division es", resultado)
    resultado = n1*n2
    print("La multiplicacion", resultado)