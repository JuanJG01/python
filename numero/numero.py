import random

def adivina_numero():
    print("Piensa en un número del 1 al 100.")
    input("Presiona Enter cuando estés listo para que adivine...")

    limite_inferior = 1
    limite_superior = 100
    intentos = 0
    adivinado = False

    while not adivinado:
        intento = random.randint(limite_inferior, limite_superior)
        print("¿Es este tu número?", intento)
        respuesta = input("¿Es más alto (h), más bajo (l) o he acertado (a)? ").lower()

        if respuesta == 'a':
            print("¡Genial! He adivinado tu número en", intentos, "intentos.")
            adivinado = True
        elif respuesta == 'h':
            limite_inferior = intento + 1
            intentos += 1
        elif respuesta == 'l':
            limite_superior = intento - 1
            intentos += 1
        else:
            print("Por favor, responde 'h', 'l' o 'a'.")

adivina_numero()