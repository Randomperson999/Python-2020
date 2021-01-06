import time
import sys
def slowText(text, speed = 0.03, wait = 0.2):

    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(wait)
    print()
def getInput(question, minLen, maxLen):
    while True:
        slowText(question)
        pInput = input()
        if len(pInput) >= minLen and len(pInput) <= maxLen:
            return pInput
        elif len(pInput) < minLen:
            slowText(str.format("Input must be at least {} characters.", minLen))
        elif len(pInput) > maxLen:
            slowText(str.format("Input must be shorter than {} characters.", maxLen + 1))
def getNum(question, low, high):
    """Gets a number and a range that it can be accepted in."""
    responce = None
    while True:
        slowText(question)
        response = input()
        if response.isnumeric() and int(response) in range(low, high):
            response = int(response)
            break
        else:
            slowText(str.format("Please enter a number between {} and {}.", low, high - 1))
    return (response)
def yesOrNo(question, minLen, maxLen):
    while True:
        slowText(question)
        pInput = input().UPPER
        if len(pInput) >= minLen and len(pInput) <= maxLen:
            if pInput == "YES" or pInput == "NO":
                pInput == pInput.lower
                return pInput
            elif pInput == "Y":
                pInput == "yes"
                return pInput
            elif pInput == "N":
                pInput == "no"
                return pInput
        elif len(pInput) < minLen:
            slowText(str.format("Input must be at least {} characters.", minLen))
        elif len(pInput) > maxLen:
            slowText(str.format("Input must be shorter than {} characters.", maxLen + 1))
class Player(object):
    def __init__(self, name, lives1 = 3):
        self.name = name
        self.score = Score()
        self.lives = lives1
class Score(object):
    def __init__(self, step = 10):
        self.value = 0
        self.stepValue = step
    def addTo(self, itemId):
        for i in range(itemId):
            self.value+=self.stepValue
    def takeFrom(self, itemId):
        for i in range(itemId):
            self.value-=self.stepValue
            if self.value < 0:
                self.value = 0
if __name__ == "__main__":
    print("You ran this module (and did not 'import' it).")
    slowText(input("\n\nPress Enter to exit..."))