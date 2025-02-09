try:    
    people = int(input("¿Cuantos invitados son?: "))

    if people > 8 :
        print("Lo sentimos tendrá que esperar por una mesa.")
    else:
        print("Su mesa está disponible")
except ValueError:
    print("Ingresa un numero válido.")