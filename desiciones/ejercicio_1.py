'''Escribir dos funciones que resuelvan los siguientes problemas:'''

'''a) Dado un número entero 𝑛, indicar si es par o no.'''

#no m esta diciendo en que forma indicar que es un entero opto por imprimirlo
def validar_entero(n):
    if n%2 ==0:
        print("El numero", n, "es par")
    else:
        print("El numero", n, "es impar")


print (validar_entero(4))

'''b) Dado un número entero 𝑛, indicar si es primo o no.'''
#un numero es primo si es mayor que 1 
#y solo tiene dos divisores posibles
#uno y el mismo

def validar_primo(n):
    cantidad_de_divisores = 0
    divisor = 1
    while divisor<n:
        divisor = divisor +1
        if n%divisor == 0:
            cantidad_de_divisores = cantidad_de_divisores + 1

    if cantidad_de_divisores > 1:
        print ("El numero", n, "no es primo")
    else:
        print("El numero", n, "es primo")


print (validar_entero(4))

print (validar_primo(13))
print (validar_primo(35))
