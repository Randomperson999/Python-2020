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