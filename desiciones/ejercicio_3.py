'''Escribir una función que reciba por parámetro una dimensión 𝑛, e imprima la
matriz identidad correspondiente a esa dimensión.'''

#recordar que el end garantiza que el cursor pemanece en la misma linea, si no se pone
#avanza a la segunda linea
def imprimir_identidad (n):
    for i in range (n):
        for j in range (n):
            if i==j:
                print("1", end=' ')
            else:
                print("0", end=' ')
        print()

imprimir_identidad(5)
