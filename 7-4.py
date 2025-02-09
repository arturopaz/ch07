prompt = "\nIngresa los ingredientes que deseas: "
pizza_toppings = []

while True:
    topping = input("Ingresa ingrediente: ").lower()

    if topping == 'quit':
        print("\nTus ingredientes son:")
        for pizza_toppin in pizza_toppings:
            print(f"\t{pizza_toppin}")
        print("Buen provecho!")
        break
    else:
        print(f"Agregaste {topping}")
        pizza_toppings.append(topping)

