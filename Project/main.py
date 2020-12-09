# Read It
# Caleb Keller
import sys
import time
from datetime import datetime
# Functions:

def slowText(text, speed=.03, sleeping=0.3):
#This is so you have the option to put in slower or faster text.
#The defaults are 0.03, and 0.3.
    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(sleeping)
def getInput(question, minLength, maxLength):
    """Gets a specific input for something."""
    time = datetime.now()
    testTime = time.strftime("%m/%d %H:%M")
    while True:
        slowText(question)
        pInput = input()
        if len(pInput) >= minLength and len(pInput) <= maxLength:
            return pInput, testTime
        elif len(pInput) < minLength:
            slowText(str.format("Input must be at least {} characters.", minLength))
        elif len(pInput) > maxLength:
            slowText(str.format("Input must be shorter than {} characters.", maxLength+1))
def getNum(question,low, high):
    """Gets a number and a range that it can be accepted in."""
    responce = None
    while True:
      slowText(question)
      response = input()
      if response.isnumeric() and int(response) in range(low, high):
          response = int(response)
          break
      else:
          slowText(str.format("Please enter a number between {} and {}.", low, high-1))
    return(response)
def welcome(title, name, testTime):
    """Welcome the player"""
    slowText("Welcome "+name+" "+"to your T E S T.\n")
    slowText(""+title)
    
def openFile(fileName, mode):
    try:
        file = open("assets/test/"+fileName, mode)
    except IOError as e:
        print("Unable to open the file", fileName, "Ending program. \n", e)
        try:
            file = open("assets/errors/errorLog.txt", "a+")
            time = datetime.now()
            errorTime = time.strftime("%m/%d/%y %H:%M:%S")
            file.write(str(e)+" " +str(errorTime)+"\n")
            slowText("\n\nPress enter to exit.")
            input()
            sys.exit()
        except:
            sys.exit()
    else:
        return file
def nextLine(file):
    try:
        line = file.readline()
        line = line.replace ("/", "\n")
        return line
    except:
        slowText("Could not read line")
        sys.exit()
def nextQuestion(file):
    """Rerurn next questions block of data from the trivia file"""
    category = nextLine(file)
    question = nextLine(file)
    answers = []
    for i in range(4):
        answers.append(nextLine(file))
    correct = nextLine(file)
    if correct:
        correct = correct[0]
    explanation = nextLine(file)
    return category, question, answers, correct, explanation
def createReportCard(name, testTime, score, totalQuestions):
    card = open("assets/test/report_cards"+name+".txt", "w")
    card.write("name = "+name+"\n")
    card.write("numCorrect = "+str(score)+"\n")
    percent = (score/totalQuestions)
    card.write("Percentage = "+"%"+str((percent)*100)+"\n")
    if percent >=90:
        card.write("Letter Grade = A")
    elif percent >=80:
        card.write("Letter Grade = B")
    elif percent >=70:
        card.write("Letter Grade = C")
    elif percent >=60:
        card.write("Letter Grade = D")
    elif percent >=50:
        card.write("Letter Grade = F")
    
def main():
    file = openFile("MidtermTest.txt", "r")# Will need to change name to match the test your taking
    title = nextLine(file)
    name, testTime = getInput("What's your name?:\n", 3, 13)
    welcome(title, name, testTime)
    score = 0
    totalQuestions = 0
    category, question, answers, correct, explanation = nextQuestion(file)
    while category:
        totalQuestions +=1
        slowText(category)
        slowText(question)
        for i in range(len(answers)):
            slowText(str.format("\{}: {}", i+1, answers[i]))
        # get answer
        answer = getNum("What's your answer: ", 1, 5)
        #check answer
        if int(answer) == int(correct):
            slowText("\nCorrect! ")
            score +=1
        else:
            slowText("\nWrong. ")
            slowText(explanation)
            slowText("Score: " + str(score) + "\n\n")
        category, question, answers, correct, explanation = nextQuestion(file)
    file.close()
    slowText("That was the last question!\n")
    slowText("Your final score is "+str(score))
    createReportCard(name, testTime, score, totalQuestions)
    
     
main()            
        

