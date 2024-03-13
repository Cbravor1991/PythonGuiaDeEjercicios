'''Escribir un programa que tome una cantidad 𝑚 de valores ingresados por el usuario,
a cada uno le calcule el factorial (utilizando la función escrita en el ejercicio 1.5) e imprima
el resultado junto con el número de orden correspondiente.'''

import sys

def factorial(n):
    resultado = 1
    for i in range (1, (n+1)):
        resultado*= i

    return resultado 

#no esta claro como deberia solicitarle los numeros al usuario y la condicion de corte
#vamos a suponer que le va pidiendo de a una y si pone 0 sale del programa
def main():
    orden = 1
    while True: 
        numero = int(input("Ingrese numero para calcular factorial: "))
        if numero == 0:
            print("Programa finalizado")
            sys.exit(0)
        else:
            numero = factorial(numero)
            print(orden, numero)
            orden = orden +1


main()