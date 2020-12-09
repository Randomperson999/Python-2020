#Caleb Keller
#9/29/2020-New Date: 10/5/2020
#Guess My Number
import random
maxNum = 10
numTrys = 3
name = "[Name]"
#print(theNum)#For testing, comment out when normal use happens.
win = False
print("\tWelcome to 'Guess My Number'!\n")
question = input("What difficulty would you like Easy, Medium, or Hard: ")
if question.startswith("E") or question.startswith("e"):
    maxNum = 10
    numTrys = 3
    diff = 1
elif question.startswith("M") or question.startswith("m"):
    maxNum = 50
    numTrys = 5
    diff = 2
else:
    maxNum = 100
    numTrys = 10
    diff = 3
print(str.format("""I'm thinking of a number between 1 and {0}.\n
Try to guess it in {1} attempts.\n""",str(maxNum),str(numTrys)))
theNum = random.randint(1, maxNum)
#guess 1
if diff >= 1:
    guess = int(input("Pick a number between 1 and "+str(maxNum)+": "))
    if guess == theNum:
        print("Winner!")
        win = True
    elif guess > theNum:
        print("guess lower")
    else:
        print("guess higher")

#guess 2
if not win:
    if diff >= 1:
        guess = int(input("Pick a number between 1 and "+str(maxNum)+": "))
        if guess == theNum:
            print("Winner!")
            win = True
        elif guess > theNum:
            print("guess lower")
        else:
            print("guess higher")

#guess 3
if not win:
    if diff >= 2:
        guess = int(input("Pick a number between 1 and "+str(maxNum)+": "))
        if guess == theNum:
            print("Winner!")
            win = True
        elif guess > theNum:
            print("guess lower")
        else:
            print("guess higher")

#guess 4
if not win:
    if diff >= 2:
        guess = int(input("Pick a number between 1 and "+str(maxNum)+": "))
        if guess == theNum:
            print("Winner!")
            win = True
        elif guess > theNum:
            print("guess lower")
        else:
            print("guess higher")

#guess 5
if not win:
    if diff == 3:
        guess = int(input("Pick a number between 1 and "+str(maxNum)+": "))
        if guess == theNum:
            print("Winner!")
            win = True
        elif guess > theNum:
            print("guess lower")
        else:
            print("guess higher")

#guess 6
if not win:
    if diff == 3:
        guess = int(input("Pick a number between 1 and "+str(maxNum)+": "))
        if guess == theNum:
            print("Winner!")
            win = True
        elif guess > theNum:
            print("guess lower")
        else:
            print("guess higher")

#guess 7
if not win:
    if diff == 3:
        guess = int(input("Pick a number between 1 and "+str(maxNum)+": "))
        if guess == theNum:
            print("Winner!")
            win = True
        elif guess > theNum:
            print("guess lower")
        else:
            print("guess higher")

#guess 8
if not win:
    if diff == 3:
        guess = int(input("Pick a number between 1 and "+str(maxNum)+": "))
        if guess == theNum:
            print("Winner!")
            win = True
        elif guess > theNum:
            print("guess lower")
        else:
            print("guess higher")

#guess 9
if not win:
    if diff == 3:
        guess = int(input("Pick a number between 1 and "+str(maxNum)+": "))
        if guess == theNum:
            print("Winner!")
            win = True
        elif guess > theNum:
            print("guess lower")
        else:
            print("guess higher")




#Final Guess

if not win:
    guess = int(input("Pick a number between 1 and "+str(maxNum)+": "))
    if guess == theNum:
        print("Winner!")
        win = True
    elif guess > theNum:
        print("You lose!, the number was "+str(theNum)+".")
    else:
        print("COnGraTulAtiOns yOu fAiLed!\nThe number was "+str(theNum)+".")

    if win:
        print("Great job!")
    else:
        print("Better luck next time")


    

