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

#print (bisiesto (2000))

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
          cantidad_dias = 0
     
     return cantidad_dias

#print(cant_dias_mes(2,2000))

'''c) Dada una fecha (día, mes, año), indicar si es válida o no '''

def validar_fecha (dia, mes, anio):
 
     if (dia< 1 or dia > 31) or (anio<0) or (mes< 1 or mes > 12) or ( dia>(cant_dias_mes(mes, anio))) :
          return "fecha incoreccta"
     else:
          return "fecha correcta"
     

#print(validar_fecha(20,2,2000))

'''
d) Dada una fecha, indicar los días que faltan hasta fin de mes
     Nota: En caso de ser una fecha invalida devolvera -1

'''

def dias_restantes_mes (dia, mes, anio):
     if (validar_fecha(dia, mes, anio)!= "fecha correcta"):
          dias_restantes = -1
     else:
          dias_totales = cant_dias_mes (mes, anio)
          dias_restantes = dias_totales - dia
     
     return dias_restantes

#print(dias_restantes_mes(18,4,2024))

'''e) Dada una fecha, indicar los días que faltan hasta fin de año.
      Nota: En caso de ser una fecha invalida devolvera -1
'''

def dias_restantes_anio(dia, mes, anio):
        if (validar_fecha(dia, mes, anio)== "fecha correcta"):
               if (bisiesto(anio)!="bisiesto"):
                    dias_totales_anio = 365
               else:
                    dias_totales_anio = 366
                   
               for i in range (1, mes):
                     dias_totales_anio = dias_totales_anio -(cant_dias_mes(i, anio))
               dias_totales_anio = dias_totales_anio - dia
        else:
              dias_totales_anio = -1

        return dias_totales_anio
             

                    

#print (dias_restantes_anio(21,4,2024))

'''f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha'''

def dias_del_anio(dia, mes,anio):
     if(validar_fecha(dia, mes, anio)== "fecha correcta"):
          dias_totales = 0
          for i in range (1, mes):
               dias_totales = dias_totales + cant_dias_mes(i, anio)
          dias_totales = dias_totales + dia
          
     return dias_totales
               
               
#print (dias_del_anio(20,6,2020))  
      

'''g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido
entre ambas, en años, meses y días.
Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.
'''

def tiempo_transcurrido(dia1, mes1, anio1, dia2, mes2, anio2):
     if ((validar_fecha(dia1, mes1, anio1)== "fecha correcta")and (validar_fecha(dia2, mes2, anio2)== "fecha correcta")):
          if (anio1<anio2) and (mes2>mes1) and (dia2>dia1):
               anio = anio2 - anio1
               mes = mes2 - mes1
               print(dias_restantes_anio(dia1, mes1, anio1))
               print(dias_restantes_anio(dia2, mes2, anio2))
               dias = dias_restantes_anio(dia2, mes2, anio2) - dias_restantes_anio(dia1, mes1, anio1)
               print(dias)
               return anio, mes, dias
               
               
               
 
tiempo_transcurrido(20,6,2020, 21,7,2021)
        
               
          