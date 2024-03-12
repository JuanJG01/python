from geometria.areas import area_cuadrado, area_triangulo, area_circulo
from geometria.perimetros import perimetro_cuadrado, perimetro_triangulo, perimetro_circulo

lado_cuadrado = 5
base_triangulo = 3
altura_triangulo = 4
radio_circulo = 2

print("Áreas:")
print("Área del cuadrado:", area_cuadrado(lado_cuadrado))
print("Área del triángulo:", area_triangulo(base_triangulo, altura_triangulo))
print("Área del círculo:", area_circulo(radio_circulo))

print("\nPerímetros:")
print("Perímetro del cuadrado:", perimetro_cuadrado(lado_cuadrado))
print("Perímetro del triángulo:", perimetro_triangulo(base_triangulo, altura_triangulo, lado_cuadrado))
print("Perímetro del círculo:", perimetro_circulo(radio_circulo))
