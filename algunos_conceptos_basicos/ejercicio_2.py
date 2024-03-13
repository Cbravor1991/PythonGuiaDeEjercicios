'''
Utilizando la función del ejercicio anterior, escribir un programa (un archivo .py)
que pida al usuario dos números, y luego muestre el producto.

'''

def producto(n1, n2):
    return (n1*n2)

#input devuelve string cuando ejecutas explota
#antes tenes que castear a int, float, etc
def main ():
    n1 = int(input ("Ingresa n1: "))
    n2 = int(input ("Ingresa n2: "))
    resultado_producto = producto(n1,n2)
    print(resultado_producto)

if __name__ == "__main__":
    main()


