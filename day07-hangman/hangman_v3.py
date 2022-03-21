# Step 3
#TO DO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
import random

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

print("     The word is: ", display, "\n")
while end_of_game == False:
    
    guess = input("Guess a letter: ").lower()

    for i in range(display_len):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = str(letter)

    
    print("     The word is: ", display, "\n")


    if "_" not in display:
        print("You won!")
        end_of_game = True
