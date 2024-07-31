"a) Escribir una función que reciba dos vectores y devuelva su producto escalar"
def producto_escalar(vec_1, vec_2):
    respuesta = 0
    for i in range (len(vec_1)):
     
        respuesta+= vec_1[i]*vec_2[i]
    
    return respuesta 
    
    