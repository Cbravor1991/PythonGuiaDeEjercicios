'''Usando las funciones del ejercicio anterior, escribir un programa que pida al usuario
dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre
por pantalla la duración total en horas, minutos y segundos.'''

def duracion_segundos(horas, minutos, segundos):
    rta_segundos = horas*3600 + (minutos*60) + segundos
    return rta_segundos

def duracion_horas(horas, minutos, segundos):
    rta_horas = horas +(minutos/60)+ (segundos/3600)
    return rta_horas

#falta la funcion para calcular minutos
def duracion_minutos(horas, minutos, segundos):
    rta_minutos = (horas*60) +(minutos)+ (segundos/60)
    return rta_minutos

def main():
    segundos = 0
    minutos = 0
    horas = 0
    for i in range (2):
        segundos_recibidos = int(input("Ingrese los segundos que desea contabilizar: "))
        minutos_recibidos = int(input("Ingrese los minutos que desea contabilizar: "))
        horas_recibidos = int(input("Ingrese los horas que desea contabilizar: "))
        segundos = duracion_segundos (horas_recibidos, minutos_recibidos, horas_recibidos) + segundos
        minutos = duracion_minutos (horas_recibidos, minutos_recibidos, horas_recibidos) + segundos + minutos
        horas = duracion_horas(horas_recibidos, minutos_recibidos, horas_recibidos) + horas

    print("La duración total en segundos es: ", segundos)
    print("La duracion total en minutos es: ", minutos)
    print("La duracion total en horas es: ", horas)        

main()

