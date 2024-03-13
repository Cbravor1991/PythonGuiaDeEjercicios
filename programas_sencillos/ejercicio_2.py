'''Utilizando la función del ejercicio anterior, escribir un programa que le pregunte
al usuario la cantidad de pesos inicial, la tasa de interés y el número de años y muestre el monto
final a obtener.'''

def interes(cantidad_pesos, tasa_interes, numero_anios):
    capital_final = (cantidad_pesos)*((1+(tasa_interes/1000))**numero_anios) 
    return capital_final

def main():
    cantidad_pesos = int(input("Ingrese la cantidad de pesos inicial: "))
    tasa_de_interes = int(input("Ingrese la tasa de interes: "))
    numero_de_anios = int(input("Ingrese el numero de años: "))
    resultado = interes(cantidad_pesos, tasa_de_interes, numero_de_anios)

    print("El monto obtenido es: ", resultado)

main()