"a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad"
"de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que"
"hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}."

def devolver_apariciones (cadena):
    palabras = cadena.split()
    diccionario = {}
    for palabra in palabras:
        if palabra not in diccionario:
            diccionario[palabra] = 1
        else:
            diccionario[palabra] +=1
        
    return diccionario

#print (devolver_apariciones("hoy es un dia hoy es sabado hoy es lunes dia "))

"b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena"
"de texto, y los devuelva en un diccionario."

def devolver_apariciones_caracter (cadena):
    diccionario = {}
    for caracteres in cadena:
        if caracteres not in diccionario:
            diccionario[caracteres] = 1
        else:
            diccionario[caracteres] +=1
        
    return diccionario


#print (devolver_apariciones_caracter("mmm hmh dhmm smsdh "))

"c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a"
"realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos"
"dados."
"Nota: utilizar el módulo random para obtener tiradas aleatorias."

import random

def sumar_dados(tiradasDados):
    diccionario = {}
    for i in range (1, tiradasDados+1):
        dado_uno = random.randint(1, 6)
        dado_dos = random.randint(1, 6) 
        suma = dado_uno + dado_dos
        if suma in diccionario:
            diccionario[suma]+=1
        else:
            diccionario[suma] = 1
            
    return diccionario
        
print(sumar_dados(25))
        