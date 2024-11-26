'''Escribir una función empaquetar para una lista, donde epaquetar significa indicar
la repetición de valores consecutivos mediante una tupla (valor, cantidad de repeticiones). Por
ejemplo, empaquetar([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devolver [(1, 3), (3, 1), (5, 1)
, (1, 2), (3, 2)].'''

def empaquetar(lista):
    empaquetado = []
    valor_actual = lista[0]
    contador = 1

    for i in range(1, len(lista)):  # Empezamos desde el segundo elemento
        if lista[i] == valor_actual:
            contador += 1  # Incrementamos el contador si es el mismo valor
        else:
            empaquetado.append((valor_actual, contador))  # Guardamos la tupla
            valor_actual = lista[i]  # Cambiamos el valor actual
            contador = 1  # Reiniciamos el contador

    # Agregar la última secuencia
    empaquetado.append((valor_actual, contador))
    
    return empaquetado
        