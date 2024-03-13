'''
Modificar el programa anterior para que pueda generar fichas de un juego que
puede tener números de 0 a 𝑛.

'''

def main():
    numero_de_fichas = int(input("Ingresa el numero de fichas del juego: "))
    for i in range (numero_de_fichas+1):
        #el secreto es ir acotando el rango a medida que se vaya avanzando con las fichas de domino
        #de esa manera no se vuelve a poner por ejemplo 0-1 y 1-0 que serian las mismas ficha
        #pero invertida 
        for j in range (i, numero_de_fichas+1):
            print(i, "-", j)

main()