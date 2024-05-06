def es_primo(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def triangulo(numero):
    primos = [i for i in range(2, numero + 1) if es_primo(i)]
    for i in range(len(primos)):
        for j in range(i, -1, -1):
            print(primos[j], end=" ")
        print()

numero = int(input("Por favor, ingresa un número entero primo: "))
if es_primo(numero):
    triangulo(numero)
else:
    print("El número ingresado no es primo.")
