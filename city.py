prompt = "\nPlease enter the name of the a city you have visited."
prompt += "\nEnter 'quit' when you finished."

while True:
    city = input("Enter city: ")

    if city != 'quit':
        print(f"I'd love to go to {city}")
    else:
        print("Quiting....")
        break
