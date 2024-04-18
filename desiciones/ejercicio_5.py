'''Escribir funciones que resuelvan los siguientes problemas:'''

'''a) Dado un año indicar si es bisiesto.
Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100,
excepto que también sea divisible por 400.'''

def bisiesto (anio):
    if ((anio %4 == 0) and anio % 100!=0):
         respuesta = "bisiesto"
    elif ((anio %4 == 0) and (anio % 100==0) and (anio%400==0)):
         respuesta = "bisiesto"
    else:
         respuesta = "no bisiesto"
    
    return respuesta

print (bisiesto (2000))

'''b) Dado un mes y un año, devolver la cantidad de días correspondientes.
 '''
# Esta practica se trata de desiciones osea para practicar if, por lo tanto
#no voy usar la libreria calander que me permite obtener los dias de un mes 
# de un año automaticamente

def cant_dias_mes (mes, anio):
     cantidad_dias = 0
     if mes == 1:
          cantidad_dias = 31
     elif ((mes == 2) and (bisiesto (anio)!= "bisiesto")):
          cantidad_dias = 28
     elif ((mes == 2) and (bisiesto (anio)== "bisiesto")):
          cantidad_dias = 29
     elif (mes == 3):
          cantidad_dias = 31
     elif (mes == 4):
          cantidad_dias = 30
     elif (mes == 5):
          cantidad_dias = 31
     elif (mes == 6):
          cantidad_dias = 30
     elif (mes == 7):
          cantidad_dias = 31
     elif (mes == 8):
          cantidad_dias = 31
     elif (mes == 9):
          cantidad_dias = 30        
     elif (mes == 10):
          cantidad_dias = 31
     elif (mes == 11):
          cantidad_dias = 30
     elif (mes == 12):
          cantidad_dias = 31
     else:
          cant_dias = 0
     
     return cantidad_dias

print(cant_dias_mes(2,2001))

