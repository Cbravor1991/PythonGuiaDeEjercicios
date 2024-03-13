'''Escribir una función que, dados cuatro números, devuelva el mayor producto de
dos de ellos. Por ejemplo, si recibe los números 1, 5, -2, -4 debe devolver 8, que es el producto
más grande que se puede obtener entre ellos (8 = −2 × −4).'''

def producto(n1, n2, n3, n4):
    return max (n1*n2, n1*n3, n1*n4, n2*n3, n2*n4, n3*n4 )
