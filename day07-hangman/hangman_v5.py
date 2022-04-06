# Step 5
"""
This is the fifth version of the hangman game.
The user can guess a letter or a word.
The user can guess wrong 6 times and the game is over.

"""
import random
import hangman_words
import hangman_art

lives = 6
chosen_word = random.choice(hangman_words.word_list)
display_len = len(chosen_word)
display = []
for i in range(display_len):
    display += "_"
end_of_game = False
print(hangman_art.logo)
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
    print(hangman_art.stages[lives])
    print("----------------------------------------------------")