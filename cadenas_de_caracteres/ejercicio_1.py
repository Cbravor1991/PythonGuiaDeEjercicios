'''Escribir funciones que dada una cadena de caracteres:'''

'''a) Imprima los dos primeros caracteres.'''
def dos_primeros_caracteres (cadena_caracteres):
    print(cadena_caracteres[:2])

dos_primeros_caracteres("HOLA")

'''b) Imprima los tres últimos caracteres.'''
def ultimos_tres_caracteres (cadena_caracteres):
    print(cadena_caracteres[-3:])
    
ultimos_tres_caracteres("HOLA")


'''c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'''
def cada_dos_caracteres(cadena_caracteres):
    print(cadena_caracteres[::2])

cada_dos_caracteres("recta")

'''d) Dicha cadena en sentido inverso. Ej.: 'hola mundo!' debe imprimir '!odnum aloh'''
def invertir_cadena(cadena_caracteres):
    print(cadena_caracteres[::-1])

invertir_cadena('hola mundo!')

'''e) Imprima la cadena en un sentido y en sentido inverso. Ej: 'reflejo' imprime
'reflejoojelfer'''
def espejo (cadena_caracteres):
    print(cadena_caracteres+cadena_caracteres[::-1])
    
espejo('reflejo')
    