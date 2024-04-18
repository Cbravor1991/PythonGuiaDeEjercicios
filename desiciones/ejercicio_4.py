'''
Escribir funciones que permitan encontrar:

'''

'''a) El máximo o mínimo de un polinomio de segundo grado (dados los coeficientes a, b y
c), indicando si es un máximo o un mínimo.'''

def maximo_minimo (a, b, c):
    vertice = "maximo"
    x= (-(b/(2*a)))
    y= (a*(x**2))+(b*x)+c
    if a>0:
        vertice = "minimo"
    print(f"El polinomio tiene un {vertice} y es ({x}, {y})")


maximo_minimo(2, 4, 1)

'''b) Las raíces (reales o complejas) de un polinomio de segundo grado.
Nota: validar que las operaciones puedan efectuarse antes de realizarlas (no dividir por
cero, ni calcular la raíz de un número negativo).'''
import cmath

def raices (a,b,c):
    discriminante = (b**2)-(4*a*c)
    if a>0:
        x1 = (-b + cmath.sqrt(discriminante))/(2*a)
        x2 = (-b - cmath.sqrt(discriminante))/(2*a)
        if discriminante > 0:
          print(f"Las raices reales son: ({x1}, {x2})")
        else:
            print(f"Las raices complejas son: ({x1}, {x2})")
    else:
        print ("La operacion no puede realizarse")
            

raices(1, 5, 6)

'''c)La intersección de dos rectas (dadas las pendientes y ordenada al origen de cada recta).
Nota: validar que no sean dos rectas con la misma pendiente, antes de efectuar la operación.
'''
def interseccion (pendiente_1, ordenada_1, pendiente_2, ordenada_2):
    if (pendiente_1 == pendiente_2):
        print("La rectas tienen las mismas pendientes")
    else:
        x = (ordenada_2 - ordenada_1)/(pendiente_1-pendiente_2)
        y = (pendiente_1 * x) + ordenada_1
        print (f"La intersección es: ({x},{y})")

interseccion (2,3, -1, 5)