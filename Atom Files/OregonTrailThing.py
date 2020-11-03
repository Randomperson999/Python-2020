#OREGON TRAIL PROJECT
#Anthony Garrard // Caleb Keller
#started 11/20
import time
import sys
def LogoScreen():
  """Displays Logo, Names, and copyright"""
  logo = """
                  _____________
                 |   ___    __/
                 |  |   |  |
                 |  |   |  |
                 |  |   |  |___________________
                 |  |___|          _________   |
                 |      ________  |_________|  |
        __       |     |        |     ______   |
       |  \______|     |        |    |      \\__|
       |   _________   |________|    |
       |  |_________|          ___   |
       |___________________   |   |  |
                           |  |   |  |
                           |  |   |  |
                         __|  |___|  |
                        \\____________| """
  names = "Anthony // Caleb"
  cright = "©Shuriken Studios"
  print(logo, names, cright, sep="\n")

def Menu():
    """Returns a valid option from current menu """
    print(menuOptions)#Is it ready to test yet?
    getNumber(menuOptions, 1, len(menuOptions))#ask for what imports we need
    return(responce)

def slowText(text):

    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(0.5)
    print()

def getNumber(question,high,low):
    responce = None
    while responce not in range(low,high):
        slowText(question)
        responce = input()
    if responce.isnumeric():
        responce = int(responce)
    else:
        slowText("Please enter a number.")
        return responce

def checkValue(rightValue, value):
    """Checks to see if the value is valid or not"""
    valueType = type

def StartScreen():
    """ Displays the start menu with 3 options, start, learn, exit"""
    oBanner = """THE UNNAMED TRAIL\n-------------------"""
    print(oBanner)
    startOptions = ["(1) Travel the Trail", "(2) Learn about the Trail", "(3) End"]
    menuOptions[0:3] = startOptions[0:3]
    Menu()
    while True:
        if int(choice) == 1:#Play
            slowText("Travel the Trail")
            break
        elif int(choice) == 2:#Learn about trail
            slowText("Learn the Trail")
            break
        elif int(choice) == 3:#quit
            slowText("Quit")
            break

#Universal Variables
menuOptions = []
LogoScreen()
input()#stop to check def
StartScreen()
input()#stop to check def
