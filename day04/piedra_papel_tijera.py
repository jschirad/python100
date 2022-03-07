from sys import int_info


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

map_option = [rock, paper, scissors]
human_choice = input("Piedra, papel o tijera? (Piedra 0, Papel 1, Tijera 2) ")
import random
computer_choice = random.randint(0, 2)
print("La maquina eligio: ", computer_choice)
print("Computer choice ", map_option[computer_choice])
print("El humano eligio: ", human_choice)
print("Human choice ", map_option[int(human_choice)])
if human_choice == computer_choice:
    print("Empate")
elif (int(human_choice) == 0 and int(computer_choice) == 1) or (int(human_choice) == 1 and int(computer_choice) == 2) or (int(human_choice) == 2 and int(computer_choice) == 0):
    print("Gana Computer")
else:
    print("Gana Human")
