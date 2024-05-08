'''Escribir funciones que dada una cadena de caracteres:
'''

'''a) Devuelva solamente las letras consonantes. Por ejemplo, si recibe 'algoritmos' o
'logaritmos' debe devolver 'lgrtms'.'''
def devolver_consonantes(cadena_caracteres):
#armo una lista con las vocales
    letras_vocales = ["a", "e", "i", "o", "u"]
    respuesta = ""
#recorro la cadena que me dan
    for letra in cadena_caracteres:
        if letra not in letras_vocales:
            respuesta+= letra
    return respuesta

print(devolver_consonantes("algoritmos"))

'''b) Devuelva solamente las letras vocales. Por ejemplo, si recibe 'sin consonantes' debe
devolver 'i ooae'.'''
def devolver_vocales(cadena_caracteres):
    #armo una lista con las vocales
    letras_vocales = ["a", "e", "i", "o", "u"]
    respuesta = ""
#recorro la cadena que me dan
    for letra in cadena_caracteres:
        if letra in letras_vocales or letra == " ":
            respuesta+= letra
    return respuesta

print(devolver_vocales("sin consonantes"))

'''c) Reemplace cada vocal por su siguiente vocal. Por ejemplo, si recibe 'vestuario' debe
devolver 'vistaerou'.'''
def reemplazo_vocales(cadena_caracteres):
    letra_vocales = ["a", "e", "i", "o", "u"]
    respuesta = ""
    for letra in cadena_caracteres:
        if letra not in letra_vocales:
            respuesta+=letra
        else:
            if letra == "u":
                respuesta+= "a"
            else:
                posicion_letra_encontrada = letra_vocales.index(letra)
                respuesta+= letra_vocales[posicion_letra_encontrada+1]
                
    return respuesta

print(reemplazo_vocales("vestuario"))           
    
    
'''d) Indique si se trata de un palíndromo. Por ejemplo, 'anita lava la tina' es un palíndromo
(se lee igual de izquierda a derecha que de derecha a izquierda).'''

def palindromo(palabra_recibida):
    #invierto y elimino los espacios en blanco
    palabra_invertida = palabra_recibida[::-1].replace(" ", "")

    if palabra_recibida.replace(" ", "") == palabra_invertida:
        return True
    else:
        return False
    
    
print(palindromo("anita lava la tina"))