'''a) Escribir una función que dado un número entero devuelva 1 si el mismo
es impar y 0 si fuera par.
b) Escribir una función que dado un número entero devuelva 0 si el mismo es impar y 1 si
fuera par.
c) Escribir una función que dado un número entero devuelva el dígito de las unidades. Por
ejemplo, para 153 debe devolver 3.
d) Escribir una función que dado un número devuelva el primer número múltiplo de 10
inferior a él. Por ejemplo, para 153 debe devolver 150.'''

#a)
def esPar(n):
    if n%2 == 0:
        return 0
    else:
        return 1

#b)
def esImpar(n):
    if n%2 != 0:
        return 0
    else:
        return 1
#c) supongo que la idea es practricar ciclos
def contar_numeros(numero):
    contador = 0
    #convierto a string
    numero_a_string = str(numero)
    #itero sobre ese string
    for i in numero_a_string:
        contador+=1

    return contador
#d) hay varias maneras de hacerlo
def multiplo_de_10(numero):
    if numero % 10 == 0:
        numero = numero - 10
        return numero
    else:
        resto = numero %10
        numero = numero - resto
        return numero