number = input("Ingrese un numero y te dire si es par o impar: ")


try:
    number = int(number)
    if number % 2 == 0:
        print(f"\nEl numero {number} es par.")
    else:    
        print(f"\nEl numero {number} es impar.")
except ValueError:
    print("\nPor favor ingrese un numero entero válido.")
