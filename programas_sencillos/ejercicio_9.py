'''
Escribir un programa que imprima por pantalla todas las fichas de dominó, de
una por línea y sin repetir.

'''

#no esta claro como se debe imprimir supongo que se debe poner numeros que representen a los puntos
# ejemplo 
#0 - 0 
#0 - 1 
# etc

def main():
    for i in range (7):
        #el secreto es ir acotando el rango a medida que se vaya avanzando con las fichas de domino
        #de esa manera no se vuelve a poner por ejemplo 0-1 y 1-0 que serian las mismas ficha
        #pero invertida 
        for j in range (i, 7):
            print(i, "-", j)

#si ya llamas al main aca no hace falta que lo llames desde el prompt cuando importas
#la funcion se ejecuta solo
main()