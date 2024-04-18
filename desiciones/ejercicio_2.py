'''Escribir una implementación propia de la función abs, que devuelva el valor absoluto
de cualquier valor que reciba.'''


def abs (n):
    if n<0:
        numero_a_string = str(n)
        numero_absoluto = numero_a_string[1:]
        resultado_numerico_absoluto = float(numero_absoluto)
    else:
        resultado_numerico_absoluto = n 
        
    return resultado_numerico_absoluto

print(abs(10))