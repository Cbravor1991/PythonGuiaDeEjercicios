'''Escribir un programa que le pida una palabra al usuario, para luego imprimirla
1000 veces, en una única línea, con espacios intermedios.
Ayuda: Investigar acerca del parámetro end de la función print'''

def main():
    palabra = input("Ingresa una palabra para imprimirla 1000 veces: ")
    for i in range (1,101):
        print(palabra, end = " ")

main()