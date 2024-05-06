def palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

palabra = input("Por favor, ingresa una palabra: ")

if palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")