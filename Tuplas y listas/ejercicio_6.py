'''Dada una lista de números enteros y un entero k, escribir una función que:'''
'''a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a
k.'''

def clasificacionDeNumeros(lista, k):
    listaMenores = []
    listaMayores = []
    listaIguales = []
    
    for i in lista:
        if k == i:
            listaIguales.append(i)
        elif i>k:
            listaMayores.append(i)
        else:
            listaMenores.append(i)
    
    return listaMenores, listaMayores, listaIguales

# Ejemplo de uso
numeros = [1, 5, 8, 3, 5, 2, 7, 5]
k = 5
menores, mayores, iguales = clasificacionDeNumeros(numeros, k)

print("Menores:", menores)
print("Mayores:", mayores)
print("Iguales:", iguales)

'''b) Devuelva una lista con aquellos que son múltiplos de k.'''

def multiplos(k, lista):
    listaMultiplos = []
    for i in lista:
        if i%k == 0:
            listaMultiplos.append(i)
    return listaMultiplos
            
# Ejemplo de uso
print(multiplos(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [3, 6, 9]          
        
    
    