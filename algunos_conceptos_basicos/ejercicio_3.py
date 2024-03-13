'''
Escribir funciones que permitan:
a) Calcular el perímetro de un rectángulo dada su base y su altura.
b) Calcular el área de un rectángulo dada su base y su altura.
c) Calcular el área de un rectángulo (alineado con los ejes 𝑥 e 𝑦) dadas sus coordenadas
𝑥1, 𝑥2, 𝑦1, 𝑦2.
d) Calcular el perímetro de un círculo dado su radio.
e) Calcular el área de un círculo dado su radio.
f) Calcular el volumen de una esfera dado su radio.
g) Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

'''
from math import pi
from math import sqrt

def perimetro_rectangulo(base, altura):
    return ((2*base)+(2*altura))

def area_rectangulo(base, altura):
    return (base* altura)

def area_rectangulo_alineado (x1, x2, y1, y2):
    base = x2-x1
    altura = y2-y1
    return (base*altura)

def perimetro_circulo(radio):
    return (2*pi*radio)

# V= (4/3)*pi*radio^3
def volumen_esfera(radio):
    return ((4/3)*(pi)*(radio)**3)

def hipotenusa (a, b):
    return sqrt((a**2)+(b**2))