'''Escribir una función que reciba una tupla de elementos si se encuentran ordenados de menor a
mayor o no'''

def verificar_orden(tupla):
    tupla_lista = list(tupla)
    tupla_ordenada = sorted(tupla)
    
    if tupla_lista == tupla_ordenada:
        return True
    else:
        return False
    
