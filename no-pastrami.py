# Lista de ordenes de sandwich
sandwich_ordenados = ['royal','filete mix','pastrami','chorizo ahumado','pastrami','super janos','royal cheese','pastrami']

#Message
print("Janos se ha quedado sin Pastrami :( ")

while 'pastrami' in sandwich_ordenados:
    sandwich_ordenados.remove('pastrami')

#Message
print("Las ordenes quedarian:")
print("======================")

for sandwich in sandwich_ordenados:
    print(f"\t{sandwich.title()}")


