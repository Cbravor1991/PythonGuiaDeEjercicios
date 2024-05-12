

'''a) Crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se
asignan en el constructor, y se imprimen como X/Y en el método __str__.'''

class Fraccion:
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor
        
    def __str__(self):
        return f"{self.dividendo/self.divisor}"
    '''b) Implementar el método __add__ que recibe otra fracción y devuelve una nueva fracción
        con la suma de ambas.'''
    
    def __add__(self, otra_fraccion):
        nuevo_dividendo = (otra_fraccion.divisor * self.dividendo)+(self.divisor * otra_fraccion.dividendo) 
        nuevo_divisor = self.divisor * otra_fraccion.divisor
        return Fraccion(nuevo_dividendo, nuevo_divisor)
    
    '''c) Implementar el método __mul__ que recibe otra fracción y devuelve una nueva fracción
        con el producto de ambas.'''
        
    def __mul__(self, otra_fraccion):
        resultado_division = (otra_fraccion.dividendo/otra_fraccion.divisor)
        nuevo_dividendo = self.dividendo * (resultado_division)
        return Fraccion(int(nuevo_dividendo), int(self.divisor))
    
    '''d) Crear un método simplificar que modifica la fracción actual de forma que los valores
    del dividendo y divisor sean los menores posibles.'''
    

   
    def simplificar (self):
        #debo hallar el maximo comun divisor que divida tanto
        #al divisor y al dividendo
        mcd = 1
        #necesito el valor menor entre el dividendo y el divisor
        for i in range (2, min(self.dividendo, self.divisor)+1):
            if self.dividendo % i == 0 and self.divisor % i==0:
                mcd = i
                break
        return Fraccion(self.dividendo/mcd, self.divisor)
        
    

    
fraccion= Fraccion (20, 10)
print (fraccion.__str__)

frac1 = Fraccion(3, 4)
frac2 = Fraccion(1, 2)

producto = frac1*frac2
suma = frac1+frac2

print("La multiplicación de las fracciones es:", producto )
print("La suma de las fracciones es:", suma )

producto_simplificado = producto.simplificar()
print("El producto simplificado es:", producto_simplificado)