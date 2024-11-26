'''a) Realizar una función que, dada una lista, devuelva una nueva lista cuyo contenido sea
igual a la original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'],
deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].'''

def invertirLista_auxiliar(lista):
    largoLista = len(lista)
    listaAuxiliar = []
    
    for i in range(largoLista - 1, -1, -1):  # Iteramos desde el final hasta el principio
        listaAuxiliar.append(lista[i])  # Añadimos el elemento en la nueva lista
    
    return listaAuxiliar

# Ejemplo de uso
lista_original = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = invertirLista_auxiliar(lista_original)

print(lista_invertida)  # Imprime: ['papa', 'a', 'día', 'buen', 'Di']



'''b) Realizar otra función que invierta la lista, pero en lugar de devolver una nueva, modifique
la lista dada para invertirla, sin usar listas auxiliares.'''
def invertirLista_sin_auxiliar(lista):
    return lista[::-1]

# Ejemplo de uso
lista_original = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = invertirLista_sin_auxiliar(lista_original)

print(lista_invertida)  # Imprime: ['papa', 'a', 'día', 'buen', 'Di']


'''# Lista original
lista = ['a', 'b', 'c', 'd', 'e']

# Crear una nueva lista en orden convencional
nueva_lista = []

for i in range(len(lista)):  # Esto recorre desde 0 hasta len(lista)-1
    nueva_lista.append(lista[i])  # Agrega el elemento correspondiente en la nueva lista

print(nueva_lista)  # ['a', 'b', 'c', 'd', 'e']'''