# Lista de ordenes de sandwich

sandwich_ordenados = ['royal','filete mix','chorizo ahumado','super janos','royal cheese']

# Lista vacia de Sandwich terminados
sandwich_terminados = []

while sandwich_ordenados:
    actual_sandwich = sandwich_ordenados.pop()
    print(f"Se esta terminando de preparar el sandwich {actual_sandwich.title()} ...")
    sandwich_terminados.append(actual_sandwich)

print("\nLista de Sandwiches Preparados:")
print("=======================")
for sandwinch in sandwich_terminados:
    print(f"\t{sandwinch.title()}")


