#Hangman

# Step 1
# Import the random module
import random

word_list = ["python", "java", "kotlin", "javascript"]

# Todo 1: Randomly choose a word from the list of words

random_word = random.choice(word_list)
guion = "_ " * len(random_word)
print("|----------------------------------------------------|")
print("|          Welcome to Hangman! let's play!           |")
print("|----------------------------------------------------|\n")

print("     The word is: ", guion, "\n")

# Todo 2: Ask the user to guess a letter

guess_letter = input("     Please, guess a letter: ")

# Todo 3: Check if the letter is in the word

for i in random_word:
    if i == guess_letter:
        print("     Good job! The letter is in the word!")
    else:
        print("     Sorry, the letter is not in the word.")

# while not guion == random_word:
#     if guess_letter in random_word:
#         print("     Good job! The letter is in the word!")

#         guion = guion.replace("_", guess_letter,)
#         print("     The word is: ", guion, "\n")
#     else:
#         print("     Sorry, but the letter is not in the word.")
#         print("     The word is: ", guion, "\n")
#         guess_letter = input("     Please, guess a letter: ")