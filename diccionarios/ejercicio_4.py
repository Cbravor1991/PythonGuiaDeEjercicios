'''Escribir una función que reciba un texto y para cada caracter presente en el texto
devuelva la cadena más larga en la que se encuentra ese caracter.'''

#supongo a libre interpretacion que cada palabra es una cadena
def encuentre_caracter(texto):
    diccionario = {}
    diccionario_caracter = {}
    palabras = texto.split()
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
        
    for palabra in palabras:
        for caracter in palabra:
            if (caracter not in diccionario_caracter):
                diccionario_caracter[caracter]=0
                
    for caracter in diccionario_caracter:
        for clave, valor in diccionario.items():
            if caracter in clave:
                if valor > diccionario_caracter[caracter]:
                    diccionario_caracter[caracter] = valor
                    
    for clave, valor in diccionario_caracter.items():
        print(clave, valor)       
    
    
encuentre_caracter("HOLA MUNDO")   