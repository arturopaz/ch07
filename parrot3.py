prompt = "\nTell me something, and I will repeat it back to you:"
prompt+= "\nEnter 'quit' to end the program. => "


active = True

while active:
    message = input(prompt).lower()

    if message != 'quit':
        print(message)
    else:
        active = False

print("Quitting the program ...")