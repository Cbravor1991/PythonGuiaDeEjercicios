'''Ejercicio 7.5. Dada una lista de números enteros, escribir una función que:
a) Devuelva una lista con todos los que sean primos.'''

def esPrimo (n):
    cantidadDeDivisores = 0
    divisor = 1
    while divisor <=n:
        if n % divisor == 0:
            cantidadDeDivisores = cantidadDeDivisores + 1
        
        divisor = divisor +1
            
    if cantidadDeDivisores == 2:
        return True
    else:
        return False
    
        
def devuelveLista (lista):
    listaRespuesta = []
    for i in lista:
        if esPrimo(i):
            listaRespuesta.append(i)
    return listaRespuesta
    

print (devuelveLista([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]))

'''b) Devuelva la sumatoria y el promedio de los valores.'''

def sumatoriaPromedio (lista):
    suma = 0
    promedio = 0
    cantidadElementos = len(lista)
    for i in lista:
        suma = suma + i
    
    promedio = suma/cantidadElementos
    
    return suma, promedio
    
    
print(sumatoriaPromedio([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]))

'''c) Devuelva una lista con el factorial de cada uno de esos números.'''

def factorial(lista):
    listaRespuesta = []

    for i in lista:
        factorial = 1
        if i >1:
            for j in range (2, i+1):
                factorial =  factorial * j
        listaRespuesta.append(factorial)
     
    return listaRespuesta

print(factorial([1, 0]))
            
            
                
            
