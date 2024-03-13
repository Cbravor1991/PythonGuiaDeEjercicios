'''Escribir una función que reciba las coordenadas de un vector en ℝ3 (x,y,z) y devuelva
la norma del vector, dada por sqtr((x^2+y^2+z^2))
Ejemplo: norma(3, 2, -4) → 5.3851'''

from math import sqrt
def norma(x,y,z):
   return sqrt((x**2)+ (y**2)+(z**2))

'''Escribir una función que reciba las coordenadas de dos vectores en ℝ3 (x1,y1,z1,x2,
y2,z2) y devuelva las coordenadas del vector diferencia (debe devolver 3 valores numéricos).
Ejemplo: diferencia(8, 7, -3, 5, 3, 2) → (3, 4, -5)'''

def vector_diferencia(x1, y1, z1, x2, y2, z2):
   return ((x1-x2), (y1-y2), (z1-z2))
   
'''Escribir una función que reciba las coordenadas de dos vectores en ℝ3 y devuelva las
coordenadas del producto vectorial, definido como:
⃗(⃗⃗⃗𝑥⃗⃗⃗⃗⃗1⃗⃗⃗⃗⃗,⃗⃗⃗⃗𝑦⃗⃗⃗⃗⃗⃗1⃗⃗⃗⃗,⃗⃗⃗⃗⃗𝑧⃗⃗⃗⃗1⃗⃗⃗⃗⃗)⃗⃗⃗ × ⃗(⃗⃗⃗𝑥⃗⃗⃗⃗⃗2⃗⃗⃗⃗⃗,⃗⃗⃗⃗𝑦⃗⃗⃗⃗⃗⃗2⃗⃗⃗⃗,⃗⃗⃗⃗⃗𝑧⃗⃗⃗⃗2⃗⃗⃗⃗⃗)⃗⃗⃗ = ⃗(⃗⃗⃗𝑦⃗⃗⃗⃗⃗1⃗⃗⃗⃗⃗𝑧⃗⃗⃗⃗⃗2⃗⃗⃗⃗⃗⃗⃗−⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗𝑧⃗⃗⃗⃗1⃗⃗⃗⃗⃗𝑦⃗⃗⃗⃗⃗2⃗⃗⃗⃗⃗,⃗⃗⃗⃗⃗⃗⃗𝑧⃗⃗⃗⃗1⃗⃗⃗⃗⃗𝑥⃗⃗⃗⃗⃗2⃗⃗⃗⃗⃗⃗⃗−⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗𝑥⃗⃗⃗⃗⃗1⃗⃗⃗⃗⃗𝑧⃗⃗⃗⃗⃗2⃗⃗⃗⃗,⃗⃗⃗⃗⃗⃗⃗𝑥⃗⃗⃗⃗⃗⃗1⃗⃗⃗⃗𝑦⃗⃗⃗⃗⃗2⃗⃗⃗⃗⃗⃗⃗−⃗⃗⃗⃗⃗⃗⃗⃗⃗⃗𝑦⃗⃗⃗⃗⃗⃗1⃗⃗⃗⃗𝑥⃗⃗⃗⃗⃗2⃗⃗⃗⃗⃗)⃗⃗⃗
Ejemplo: producto_vec(1, 4, -2, 3, -1, 0) → (-2, -6, -13)'''

def producto_vectorial(x1, y1, z1, x2, y2, z2):
   return ((y1*z2-z1*y2), (z1*x2-x1*z2), (x1*y2-y1*x2))


'''Utilizando las funciones anteriores, escribir una función que reciba las coordenadas de
3 puntos en ℝ3 y devuelva el área del triángulo que conforman.
Ayuda: Si 𝐴, 𝐵 y 𝐶 son 3 puntos en el espacio, la norma del producto vectorial ⃗𝐴⃗𝐵⃗ × ⃗𝐴⃗𝐶⃗ es
igual al doble del área del triángulo 􀀀
𝐴𝐵𝐶.
Ejemplo: area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0) → 19.4551'''

def area_trinangulo(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    (a, b, c) = producto_vectorial(b1 - a1, b2 - a2, b3 - a3, c1 - a1, c2 - a2, c3 - a3)
    norma = sqrt(a ** 2 + b ** 2 + c ** 2) 
    return (norma / 2)

'''Escribir una función que reciba las coordenadas de 4 puntos en el plano ℝ4 (x1,y1,x2,
y2,x3,y3,x4,y4) que conforman un cuadrilátero convexo, y devuelva el área del mismo.
Ayuda: Aprovechar las funciones escritas anteriormente, asumiendo que los puntos dados
están en ℝ3 con coordenada 𝑧 = 0.
Ejemplo: area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5) → 65
'''

def area_cuadrilatero(x1, y1, x2, y2, x3, y3, x4, y4):
    primer_triangulo = area_trinangulo(x1, y1, 0, x2, y2, 0, x3, y3, 0)
    segundo_triangulo = area_trinangulo(x1, y1, 0, x3, y3, 0, x4, y4, 0)
 
    return (primer_triangulo+segundo_triangulo)


print (area_cuadrilatero(4, 3, 5, 10, -2, 8, -3, -5))