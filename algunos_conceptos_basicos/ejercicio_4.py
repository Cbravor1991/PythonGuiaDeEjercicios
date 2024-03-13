'''
Analizar los siguientes bloques de código. ¿Cuál será el resultado de ejecutarlos?
Verificar la respuesta con el intérprete.
a) for i in range(5):
print(i * i)
b) for i in range(2, 6):
print(i, 2 ** i)

'''

#a) El bloque for va a imprimir por pantalla el valor que van a ir adquiriendo las i multiplicadas pos si mismas (i*i)
#los valores que van a tomar las i van desde 0 hasta 4, ya que el rango es hasta 5 (no inclusive) , 
#por lo tanto los valores que van a adquirir las i se encuentran dentro del rango {0,1,2,3,4}

def a():
    for i in range(5):
        print(i*i)

#b) El bloque for va a imprimir, el valor de i junto con el valor de 2 elevado al valor de i, los valores que va a tomar
# se enceuntran en el rango que va desde 2 (ya que lo indica) hasta 6 (no inclusive), entonces los valores que i
#va a tomar {2,4,5}
        
def b():
    for i in range(2, 6):
        print(i, 2 ** i)
