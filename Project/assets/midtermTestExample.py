# Midterm Test Test
# Trivia game that reads plain text file
# Jadiah J 12/03/20

# imports
import sys
from datetime import datetime

# functions
def openFile(file_name, mode):
    """ opens and returns an open file with a given permission """
    try:
        file = open("Assets/Test_Files/" + file_name, mode)
    except IOError as e:
        print("Unable to open file", file_name, "Ending program \n", e)
        try:
            file = open("Assets/Errors/errors_log.txt", "a+")
            time = datetime.now()
            errorTime = time.strftime("%m/%d/%Y %H:%M:%S")
            file.write(str(e)+" "+str(errorTime)+"\n")
            input("\n\nPress Enter to exit")
            sys.exit()
            
        except:
            sys.exit()
    else:
        
        return file

def nextLine(file):
    try:
        line = file.readline()
        line = line.replace("/", "\n")
        return line
    except:
        print("Could not read line")
        sys.exit()
    
def nextQuestion(file):
    """Return the next question block of data from the trivia file"""
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

def getName():
    try:
        time = datetime.now()
        testTime = time.strftime("%m/%d/%Y %H:%M")
        while True:
                name = input("What is your name: ")
                if len(name) >= 3 and " " in name:
                    name = name.title()
                    return name, testTime
    except:
        print("Unable to get name \tEnding program")
        sys.exit()

def welcome(title, name, testTime):
    """Welcomes player"""
    print("Welcome, " + name + ", " + "to your Mid Term\n")
    print("Your test is " + title)

def reportCard(name, score, totalQuestions):
    line = ("________________________________________________________")
    nameInFile = name.replace(" ", "_")
    percentage = ((score/totalQuestions)*100)
    card = open("Assets/" + nameInFile + "Report_Card" + ".txt", "w")
    card.write("\tThis is " + name + "'s Report Card\n")
    card.write(line + "\n\n")
    card.write("Student Name = " + name + "\n")
    card.write("Correct = " + str(score) + "\n")
    card.write("Percentage = %" + str((score/totalQuestions)*100) + "\n")
    if percentage >= 90:
        card.write("Letter Grade = A")
    if percentage >= 80 and percentage < 90:
        card.write("Letter Grade = B")
    if percentage >= 70 and percentage < 80:

        card.write("Letter Grade = C")
    if percentage >= 60 and percentage < 70:
        card.write("Letter Grade = D")
    if percentage < 60:
        card.write("Letter Grade = F")

def main():
    file = openFile("Midterm_Test.txt", "r")# will need to change file to match the test that you're taking
    title = nextLine(file)
    name, testTime = getName()
    welcome(title, name, testTime)
    score = 0
    totalQuestions = 0
    category, question, answers, correct, explanation = nextQuestion(file)
    while category:
        totalQuestions += 1
        print(category)
        print(question)
        for i in range(len(answers)):
            print(str.format("\t{}:  {}", i+1, answers[i]))
        playerAnswer = input("What is your answer?(Enter a number): ")
        if playerAnswer == correct:
            print("\nCorrect!", end=" ")
            score += 1
        else:
            print("\nIncorrect", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")
        # get next question block
        category, question, answers, correct, explanation = nextQuestion(file)
    file.close()
    print("That was the last question!")
    print("You're final score is", score, "out of", totalQuestions)
    reportCard(name, score, totalQuestions)

main()

