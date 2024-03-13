'''Escribir un programa que imprima todos los números pares entre dos números
que se le pidan al usuario.'''

def numeros_pares(n1, n2):
    for i in range (n1, n2+1):
        if i%2 == 0:
            print(i)
    
def main():
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: ")) 
    numeros_pares(n1, n2)

main()