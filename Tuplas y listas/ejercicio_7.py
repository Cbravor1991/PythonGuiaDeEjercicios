'''Escribir una función que reciba una lista de tuplas (Apellido, Nombre, Inicial_
segundo_nombre) y devuelva una lista de cadenas donde cada una contenga primero el
nombre, luego la inicial con un punto, y luego el apellido.'''

def listaDeCadenas(listaDeTuplas):
    listaDeCadenas = []
    for apellido, nombre, inicial_segundo_nombre in listaDeTuplas:
        cadena = f"{nombre} {inicial_segundo_nombre}. {apellido}"
        
        listaDeCadenas.append(cadena)
    return listaDeCadenas
    
# Ejemplo de uso
lista_tuplas = [
    ("García", "Juan", "A"),
    ("Pérez", "Ana", "M"),
    ("Lopez", "Carlos", "R")
]

resultado = listaDeCadenas(lista_tuplas)
print(resultado)  # ['Juan A. García', 'Ana M. Pérez', 'Carlos R. Lopez