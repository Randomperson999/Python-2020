#Caleb Keller
#9/29/2020
#Guess My Number
import random
theNum = random.randint(1, 10)
name = "[Name]"
#print(theNum)#For testing, comment out when normal use happens.
win = False
print("""\tWelcome to 'Guess My Number'!\n
I'm thinking of a number between 1 and 10.\n
Try to guess it in three attempts.\n""")
#guess
count = 2
guess = int(input("Pick a number between 1 and 10: "))

if guess == theNum:
    print("Winner!")
    win = True
elif guess > theNum:
    print("guess lower")
else:
    print("guess higher")

#guess 2
if win == False:
        guess = int(input("Pick a number between 1 and 10: "))
        if (guess == theNum) and (not win):
            print("Winner!")
            win = True
        elif guess > theNum:
            print("guess lower")
        else:
            print("guess higher")

#guess 3
if win == False:
        guess = int(input("Pick a number between 1 and 10: "))
        if (guess == theNum) and (not win):
            print("Winner!")
            win = True
        elif guess > theNum:
            print("You lost!")
            print("The number was", theNum)
        else:
            print("You failed!")
            print("The number was", theNum)
if win:
    print("Great job!")
else:
    print("Better luck next time")

    

