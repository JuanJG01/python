# Solicita al usuario que ingrese la cantidad
amount = int(input("Ingrese la cantidad a convertir en monedas: "))

# divide la cantidad ingresada y la divide entre 20 y la guarda en la variable coins_20
coins_20 = amount // 20
# Calcula el residuo y lo guarda en la variable remaining
remaining  = amount % 20

# divide el residuo entre 10 para consegir la cantidad de monedas de 10
coins_10 = remaining  // 10
# Actualiza el residuo después de usar las monedas de $10
remaining  %= 10

# Calcula la cantidad de monedas de $5
coins_5 = remaining  // 5
remaining  %= 5

# Lo que quede son monedas de $1
coins_1 = remaining 

# finalmente imprime el resultado
print("Su cambio sería de:")
print("\033[93m",coins_20,"\033[0m"," Monedas de $20")
print("\033[93m",coins_10,"\033[0m"," Monedas de $10")
print("\033[93m",coins_5,"\033[0m"," Monedas de $5")
print("\033[93m",coins_1,"\033[0m"," Monedas de $1")
