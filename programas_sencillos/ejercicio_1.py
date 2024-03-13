'''Escribir una función que reciba una cantidad de pesos, una tasa de interés y un
número de años y devuelva el monto final a obtener. La fórmula a utilizar es:
𝐶𝑛 = 𝐶 × (1 + (𝑥/100))^𝑛
Donde 𝐶 es el capital inicial, 𝑥 es la tasa de interés y 𝑛 es el número de años a calcular.'''

def interes(cantidad_pesos, tasa_interes, numero_anios):
    capital_final = (cantidad_pesos)*((1+(tasa_interes/1000))**numero_anios) 
    return capital_final
