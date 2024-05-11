
'''a) Implementar la clase Intervalo(desde, hasta) que representa un intervalo entre dos
instantes de tiempo (números enteros expresados en segundos), con la condición desde
< hasta.'''

class Intervalo:
    
    '''Se crea la clase intervalo'''
    
    def __init__(self, desde, hasta):
        '''Se inicia la clase intervalo, se chequea que los 
        datos ingresados cumplan con las restricciones necesarias
        de lo contrario lanza una excepcióm
        '''
        if desde < hasta:
            self.desde = desde
            self.hasta = hasta
        else:
            raise Exception ("Desde es mayor que hasta") 
        
    
    '''b) Implementar el método duracion que devuelve la duración en segundos del intervalo.'''
    def duración(self):
        '''Devuelve la duración en segundos del intervalo con el cual se inicio la clase'''
        return self.hasta - self.hasta
    
    '''c) Implementar el método interseccion que recibe otro intervalo y devuelve un nuevo intervalo
        resultante de la intersección entre ambos, o lanzar una excepción si la intersección es nula.'''
        
    def interseccion(self, intervalo_recibido):
        '''Devuelve un intervalo con la cota superior e inferior correspondiente a la interseccion 
            entre los dos intervalos
        '''
        if self.desde< intervalo_recibido.desde <self.hasta:
            return Intervalo(intervalo_recibido.desde, self.hasta)
        elif self.desde<intervalo_recibido.hasta < self.hasta:
                return Intervalo (self.desde, intervalo_recibido.hasta)
        else:
            raise Exception ("La intersección es nula")
        
    '''d) Implementar el método union que recibe otro intervalo. Si los intervalos no son adyacentes
        ni intersectan, debe lanzar una excepción. En caso contrario devuelve un nuevo
        intervalo resultante de la unión entre ambos.'''
        
    def union (self, otro_intevalo):
        '''Este metodo estudia si los intervalos son adyacentes o tienen una interseccion'''
        #entiendo por adyacente que los intervalos comparten una cota pero no se superpone
        
        if self.desde< otro_intevalo.desde <self.hasta or otro_intevalo.hasta == self.desde:
            return Intervalo(otro_intevalo.desde, self.hasta)
        elif self.desde<otro_intevalo.hasta < self.hasta or self.hasta == otro_intevalo.desde:
                return Intervalo (self.desde, otro_intevalo.hasta)
        else:
            raise Exception ("La intersección es nula")
            

try:
  
    intervalo1 = Intervalo(3, 8)
    intervalo2 = Intervalo(6, 10)
    
    #para probar las excepciones
    intervalo3 = Intervalo(1, 2)

   
    print("Intervalo 1:", intervalo1.desde, intervalo1.hasta)
    print("Intervalo 2:", intervalo2.desde, intervalo2.hasta)


    interseccion = intervalo1.interseccion(intervalo2)
    print("Intersección:", interseccion.desde, interseccion.hasta)

    union = intervalo1.union(intervalo2)
    print("Unión:", union.desde, union.hasta)
    
    #con esto salta la excepcion
    interseccion = intervalo1.interseccion(intervalo3)
    print("Intersección:", interseccion.desde, interseccion.hasta)

except Exception as e:
   
    print("Se produjo un error:", e)
            
            
    