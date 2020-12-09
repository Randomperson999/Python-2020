#### Caleb Keller ###
#### Hangman 1.0 ####
#### 10/13/2020 #####
#imports
import random
#Hangman art and lives.
HANGMAN = (
"""
|-------------
|            |
|   
|   
|    
|      
|      
|
|
|
|
|
|
|
|
|
|______________
""",
"""
|-------------
|            |
|           ___
|          /   \\
|          \\___/
|            |
|
|
|
|
|
|
|
|
|
|
|______________
""",
"""
|-------------
|            |
|           ___
|          /   \\
|          \\___/
|            |
|            |
|            |
|            |
|            |
| 
|
|
|
|
|
|______________
""",
"""
|-------------
|            |
|           ___
|          /   \\
|          \\___/
|            |
|            |
|            |
|            |
|            |
|           /
|          /
|         /
|        /
|
|
|______________
""",
"""
|-------------
|            |
|           ___
|          /   \\
|          \\___/
|            |
|            |
|            |
|            |
|            |
|           / \\
|          /   \\
|         /     \\
|        /       \\
|
|
|______________
""",
"""
|-------------
|            |
|           ___
|          /   \\
|          \\___/
|            |
|            |\\
|            | \\
|            |  \\
|            |   \\
|           / \\
|          /   \\
|         /     \\
|        /       \\
|
|
|______________
""",
"""
|-------------
|            |
|           ___
|          /   \\
|          \\___/
|            |
|           /|\\
|          / | \\
|         /  |  \\
|        /   |   \\
|           / \\
|          /   \\
|         /     \\
|        /       \\
|
|
|______________
"""
    )
#Initialize variables for life amounts (MAX_WRONG), words,
#   a random word, what was guessed so far, etc.
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("ARGUMENT", "CLASS", "IDE", "STRING", "DEBUGGER")
word=random.choice(WORDS)
so_far = " _ "*len(word)
used = []
wrong = 0
print("Welcome to Hangman.  Good luck!")
#A statement making it so the game will run until you win or lose.
while wrong < MAX_WRONG and so_far!= word:
    print("\nIncorrect Letters: ", HANGMAN[wrong])
    print("\nWord:\n",so_far)
    print("\nUsed Letters:\n", used)

    guess = input("\n\nEnter Your Guess: ")
    guess = guess.upper()
    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("\n\nEnter Your Guess: ")
        guess = guess.upper()
    used.append(guess)
#Figures out if the guessed letter is in the word or not.
    if guess in word:
        print("\nYes", guess, "is in the word!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new+=guess
            else:
                new+=so_far[i]
        so_far = new
    else:
        print("\nSorry", guess, "isn't in the word.")
        wrong += 1
#This is to check if you win or lose.
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nSo far the word is", so_far)
    print("You lost...")
else:
    print(HANGMAN[wrong])
    print("\nYou guessed it!")
    print("\nThe word was:\n", so_far)
    if so_far == WORDS[0]:
        print("Definition: A value passed to a function when calling the function.")
    if so_far == WORDS[1]:
        print("Definition: An object constructor or \"blueprint\" for creating objects.")
    if so_far == WORDS[2]:
        print("Definition: An Integrated Development Enviornment, or a program dedicated to software development.")
    if so_far == WORDS[3]:
        print("Definition: A line of text in code surrounded by quote marks.")
    if so_far == WORDS[4]:
        print("Definition: A program that can help you find out what's going on and fix errors in a program.")
input("\n\nPress enter key to exit.")

