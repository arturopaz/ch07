prompt = "\nTell me something, and I will repeat it back to you:"
prompt+= "\nEnter 'quit' to end the program.\n"

message = ''

while message != 'quit':
    message = input(prompt).lower()

    if message != 'quit':
        print(message)

print("Quitting the program ...")