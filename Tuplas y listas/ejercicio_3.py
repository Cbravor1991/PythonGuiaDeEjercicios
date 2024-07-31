"a) Escribir una función que reciba una tupla con nombres, y para cada nombre imprima"
"el mensaje Estimado <nombre>, vote por mí."

def vote_por_mi(nombres):
    '''Recibe una tupla y escribe un mensaje en particular'''
    for i in range (len(nombres)):
        print(f'Estimado {nombres[i]}, vote por mí')
        

"pruebo la función"
#vote_por_mi(('jose', 'mariano', 'sergio', 'carlos'))

"b)Escribir una función que reciba una tupla con nombres, una posición de origen p y una"
"cantidad n, e imprima el mensaje anterior para los n nombres que se encuentran a partir"
"de la posición p."

def analisis_posicion_nombre (nombres, p, n):
    for i in range (0, n):
        if p+i < len(nombres):
            print(f'Estimado {nombres[p+i]}, vote por mi')
            
#analisis_posicion_nombre(('jose', 'mariano', 'sergio', 'carlos'), 3, 3)

"c) Modificar las funciones anteriores para que tengan en cuenta el género del destinatario,"
"para ello, deberán recibir una tupla de tuplas, conteniendo el nombre y el género."

def vote_por_mi_genero(nombres):
    '''Recibe una tupla y escribe un mensaje en particular'''
    for i in range (len(nombres)):
        nombre, genero = nombres[i]
        if genero =='M':
            print(f'Estimado {nombre}, vote por mí')
        else:
              print(f'Estimada {nombre}, vote por mí')
              
#vote_por_mi_genero((('Jose', 'M'), ('Sergio', 'M'), ('Estefi', 'F'),('Katy', 'F')))

def analisis_posicion_nombre_genero (nombres, p, n):
    for i in range (0, n):
        if p+i < len(nombres):
            nombre, genero = nombres[p+i]
            if genero == 'M':
                print(f'Estimado {nombre}, vote por mi')
            else:
                print(f'Estimada {nombre}, vote por mi')
                

analisis_posicion_nombre_genero((('Jose', 'M'), ('Sergio', 'M'), ('Estefi', 'F'),('Katy', 'F')),2,2)
            
            
            
        
        
    
            
    
        
    