print("Si podrias visitar algún lugar en el mundo, ¿A que lugar irías?")
active = True
lugares = []

while active:
    lugar = input("Escribe el lugar: ").lower()
    message= input("¿Deseas seguir agregando lugares?(Sí/No):")
    
    lugares.append(lugar)

    if message == 'no':
        break

print("Tus lugares favoritos serían")
for lugar in lugares: 
    print(f"\t{lugar.title()}")