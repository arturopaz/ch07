respuestas = {}

# Fijar una bandera que indica si la encuesta esta activa.
polling_active = True

while polling_active:
    # Solicitud de nombre y respuesta
    name = input("\n¿Cual es tu nombre?: ")
    response = input("¿Que montaña te gustaria escalar algún día?: ")


    # Almacenar la respuesta in el diccionario
    respuestas[name] = response

    # Pregunar si alguien mas tomara la encuesta.
    repeat = input("¿Alguien mas tomara la encuentas (Sí/No)?: ").lower()
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--------Poll Results---------")
for name, response in respuestas.items():
    print(f"A {name.title()} le gustaría escalar {response.title()}")




