pets = ['dog','cat','rabbit','cappibara','cat', 'goldfish','cat']
print("La lista de mascotas: ")
print(pets)


while 'cat' in pets:
    pets.remove('cat')

print("La lista sin cats:")
print(pets)