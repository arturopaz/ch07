print("Parar terminar el programa escribir 'quit'.")
active = True
while active:
    
    edad = input("¿Cual es tu edad: ")

    if edad == 'quit':
        print("Saliendo del programa ...")
        active = False
    else:
        edad = int(edad)

        if edad < 3:
            cost = 0       
        elif edad <=12:
            cost = 10
        else:
            cost = 15
        print(f"El costo del ticket es {cost}")
    

