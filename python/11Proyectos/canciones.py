def obtener_letra(cancion):
    letras = {
        "Dubidubidu": """Si tú quieres bailar, jugar, pintar, cantar
Tú puedes venir a mi casa
La idea es compartir, te vas a divertir
Si quieres venir a mi casa""",
        "creeper vs zombie rap": """Tú no lo sabes, te estoy vigilando
Desde la distancia me estoy acercando
Soy una sombra y tú no te das cuenta
Hola, ¿qué tal? ¡Date la vuelta!""",
        "rosa pastel": """Sí, yo quería ser esa mujer
La madre de tus hijos
Y juntos caminar hacia el altar
Directo hacia la muerte""",
        "mil rosas para mi": """Por eso esperaba con la carita empapada
A que llegaras con rosas, con mil rosas para mí
Porque ya sabes que me encantan esas cosas
Que no importa si es muy tonto, soy así
Y aún me parece mentira que se escape mi vida
Imaginando que vuelves a pasarte por aquí
Donde los viernes cada tarde, como siempre
La esperanza dice quieta, hoy quizás sí""",
        "eres horrible vete a la versh": """Inicias la semana con un rostro amargo
Horrible como todo un perdedor
Te comes un cereal muy viejo
Después de verte al espejo, y te preguntas si la vida te dará algo mejor""",
        "el ratón vaquero": """En la ratonera ha caído un ratón
Con sus dos pistolas y su traje de cowboy
Ha de ser gringuito porque siempre habla inglés
A más de ser güerito y tener grandes los pies""",
        "el puton del barrio": """Los amigos le dicen: "marica"
Y su nombre es Rosario
Pero todos le llamamos
El Putón del barrio
                                  
Se encamó con el de la despensa
Y con el comisario
Y así fue que le quedó
El Putón del barrio""",
        "godzilla vs king kong rap": """Chitón, llegó el jodido King Kong
Puedes jugar con mis pelotas y llamarlo Ping-Pong
Sin pincharme Winstrol estoy hecho puro músculo
Los dos somos gigantes más tu poder es minúsculo
No suelo tener compasión con mis adversarios
Y además ya he roto la mandíbula a algún dinosaurio""",
        "el caballo homosexual": """Perdido en las montañas
Le gusta caminar entre las flores
Los animales le temen
Y cuando lo ven se esconden""",
         "Chacarron": """Oh yeah
Seummm soumm, yeouh, macarron
Yeah, macarron, no
Chacarron
Chacarron
Chacarron
Chacarron"""
    }
    return letras.get(cancion, "Lo siento, no encontré la letra de esa canción.")

def main():
    print("Bienvenido, por favor selecciona una canción de este top 10 de canciones:")
    print("""
    1) Dubidubidu
    2) creeper vs zombie rap
    3) rosa pastel
    4) mil rosas para mi
    5) eres horrible vete a la versh
    6) el ratón vaquero
    7) el puton del barrio
    8) godzilla vs king kong rap
    9) el caballo homosexual
    10) Chacarron
    """)
    opcion = input("Selecciona una canción: ")

    canciones = {
        "1": "Dubidubidu",
        "2": "creeper vs zombie rap",
        "3": "rosa pastel",
        "4": "mil rosas para mi",
        "5": "eres horrible vete a la versh",
        "6": "el ratón vaquero",
        "7": "el puton del barrio",
        "8": "godzilla vs king kong rap",
        "9": "el caballo homosexual",
        "10": "Chacarron"
    }

    cancion_elegida = canciones.get(opcion)
    if cancion_elegida:
        letra = obtener_letra(cancion_elegida)
        print(f"Seleccionaste {cancion_elegida}. Aquí tienes:\n{letra}")
    else:
        print("Opción inválida. Por favor, selecciona una canción válida.")

if __name__ == "__main__":
    main()
