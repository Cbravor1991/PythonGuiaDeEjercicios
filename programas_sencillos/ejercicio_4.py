'''Escribir un programa que utilice la función anterior para generar una tabla de
conversión de temperaturas, desde 0 °F hasta 120 °F, de 10 en 10.'''

def celcius(grados):
    return (95*grados + 32)

def main():
 
    print ("°F", "°C")
    for i in range(0, 13):
        resultado = celcius(10*i)
        print(10*i,resultado)
  

main()