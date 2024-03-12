def verificar_dominio(correo_electronico):
    nombre_usuario, dominio = correo_electronico.split('@')
    
    dominios_populares = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    
    if dominio.lower() in dominios_populares:
        print(f"¡Hola {nombre_usuario.capitalize()}, veo que tu correo electrónico está registrado con {dominio.capitalize()}! ¡Qué genial!")
    else:
        print(f"¡Hola {nombre_usuario.capitalize()}, parece que tienes tu propia configuración personalizada en {dominio.capitalize()}! ¡Impresionante!")

def main():
    correo_electronico = input("Ingrese su dirección de correo electrónico: ")
    verificar_dominio(correo_electronico)

if __name__ == "__main__":
    main()
