# Empieza con usuarios que necesita ser verificados
# y una ñista vacia para mantener los usuarios verificados

unconfirmed_users = ['jose','francisco','vidal']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"El usuario {current_user} has sido confirmado.")

    confirmed_users.append(current_user)

# Mostrando todos los usuarios confirmados
print("\nLa lista de usuarios confirmados: ")
for confirmed_user in confirmed_users:
    print(f"\t{confirmed_user.title()}")