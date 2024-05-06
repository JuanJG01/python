def triangulo(n):
    for i in range(1, n + 1):
        print('*' * i)

numero = int(input("Por favor, ingresa un número entero para la altura del triángulo rectángulo: "))
triangulo(numero)
