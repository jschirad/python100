import random
names_string = input("Give me everybody's names, separated by a comma. ")
# Pedimos una lista de nombres por pantalla
names = names_string.split(", ")
# Separamos la lista de nombres por comas

num_items = len(names)
# Contamos el número de elementos de la lista
random_choice = random.randint(0, num_items - 1)
# Generamos un número aleatorio entre 0 y el número de elementos de la lista

winner = names[random_choice]

print("The winner is:", winner)