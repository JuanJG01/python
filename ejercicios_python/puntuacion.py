salary = 10000

points = int(input("Introduce tu puntuación: "))

if points >= 0 and points <=3:
    level = "Inaceptable"
elif points >= 4 and points <=6:
    level = "Aceptable"
elif points >= 7:
    level = "Meritorio"
else:
    level = ""

if level == "" or points > 10:
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es: " + level)
    print("Te corresponde cobrar: " ,salary*(points/10))