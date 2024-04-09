nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
email = input("Ingresa tu correo electrónico: ")

print("Mi nombre es \033[1;32m{}\033[0m, tengo \033[1;34m{}\033[0m años y se enviará un correo electrónico a la siguiente dirección \033[1;31m{}\033[0m.".format(nombre, edad, email))