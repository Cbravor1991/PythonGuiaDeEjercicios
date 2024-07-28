"a) Escribir una función que indique si dos fichas encajan o no."
"Las fichas son recibidas en dos tuplas por ejemplo: (3,4) y (5,4)"

def encajan_domino_en_tupla(ficha_1, ficha_2):
    '''verifica si dos fichas de domino recibidas como tuplas encajan'''
    
    if ficha_1[0] in ficha_2:
        return True
    
    return False

"Probamos la función"
print(encajan_domino_en_tupla((3,4),(4,3)))
print(encajan_domino_en_tupla((0,1),(8,5)))

"b) Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son"
"recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar la función split de las"
"cadenas."

def encajan_domino_en_cadena(fichas):
    '''verifica si dos fichas de domino reibidas como una unica cadena encajan'''
    
    ficha_1, ficha_2 = fichas.split()
    ficha_1_numero_1, ficha_1_numero_2 = ficha_1.split('-')
    ficha_2_numero_1, ficha_2_numero_2 = ficha_2.split('-')
    
    if (ficha_1_numero_1 == ficha_2_numero_1 or 
    ficha_1_numero_1 == ficha_2_numero_2 or 
    ficha_1_numero_2 == ficha_2_numero_1 or 
    ficha_1_numero_2 == ficha_2_numero_2):
        return True
    return False

"Probamos la función"
print(encajan_domino_en_cadena('3-4 3-5')) 
        
    
    