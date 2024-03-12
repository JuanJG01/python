from operaciones_matematicas import suma, resta, multiplicacion, division

def solicitar_operacion():
    print("¿Qué operación desea probar?")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = input("Ingrese el número de la operación que desea probar: ")
    return int(opcion)

def realizar_operacion(opcion):
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    
    if opcion == 1:
        resultado = suma(a, b)
        print(f"Resultado de la suma: {resultado}")
    elif opcion == 2:
        resultado = resta(a, b)
        print(f"Resultado de la resta: {resultado}")
    elif opcion == 3:
        resultado = multiplicacion(a, b)
        print(f"Resultado de la multiplicación: {resultado}")
    elif opcion == 4:
        resultado = division(a, b)
        print(f"Resultado de la división: {resultado}")
    else:
        print("Opción inválida")

opcion = solicitar_operacion()
realizar_operacion(opcion)
