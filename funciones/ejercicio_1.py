'''
Escribir dos funciones que permitan calcular:
a) La duración en segundos de un intervalo dado en horas, minutos y segundos.
b) La duración en horas, minutos y segundos de un intervalo dado en segundos.

'''

def duracion_segundos(horas, minutos, segundos):
    rta_segundos = horas*3600 + (minutos*60) + segundos
    return rta_segundos

def duracion_horas(horas, minutos, segundos):
    rta_horas = horas +(minutos/60)+ (segundos/3600)
    return rta_horas




