# Step 4

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6
word_list = ["python", "java", "kotlin", "javascript"]
chosen_word = random.choice(word_list)
display_len = len(chosen_word)
display = []
for i in range(display_len):
    display += "_"
end_of_game = False
print(f'Pssst, the solution is {chosen_word}.')

print("|----------------------------------------------------|")
print("|          Welcome to Hangman! let's play!           |")
print("|----------------------------------------------------|\n")

print("The word is: ", display, "\n")
while end_of_game == False:
    
    guess = input("Guess a letter: ").lower()

    for i in range(display_len):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = str(letter)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lost!")
            end_of_game = True

    if "_" not in display:
        print("You won!")
        end_of_game = True

    print("The word is: ", display, "\n")
    print("----------------------------------------------------")
    print(stages[lives])
    print("----------------------------------------------------")