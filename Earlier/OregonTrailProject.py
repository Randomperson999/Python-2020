#OREGON TRAIL PROJECT
#Anthony Garrard // Caleb Keller
#started 11/20| (Testing code: slowText("Ya game works") )
import time
import sys
import datetime
import random
import math
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
       |  \\______|     |        |    |      \\__|
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
#Logo and copyright

def slowText(text, speed=.03, sleeping=0.3):
#This is so you have the option to put in slower or faster text.
#The defaults are 0.03, and 0.3.
    """MAKES TYPING EFFECT TEXT"""

    for char in text:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()

    time.sleep(sleeping)
    print()

def getNumber(question,high,low):
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

def learn():
    """Displays the story of the game"""
    story = """ Some time ago, the darkness was cursed. The spirit world and the Other World
have been connected to your world by the darkness. Despite all this, you and your group are venturing into
a dangerous land to find a new home. Be prepared, be careful where you go, and beware of the darkness, unless
you can appease it.
    """
    slowText(story, 0.045)



def charSetup():
    """Sets the players class and starting money"""
    pClass = ""
    classOptions = ["(1) Knight (Starts with: 1000 gold)", "(2) Wizard (Starts with 800 gold)", "(3) Bard (Starts with 400 gold)", "(4) Cultist (Starts with 300 gold)", "(5) Blacksmith (Starts with 500 gold)", "(6) Explanation of Choices"]
    while True:
        slowText("Choose a class.")
        choice = getNumber(classOptions, len(classOptions)+1, 1)
        if choice == 1:
            pClass = "Knight"
            slowText("You are a " + pClass)

            return pClass
        elif choice == 2:
            pClass = "Wizard"
            slowText("You are a " + pClass)

            return pClass
        elif choice == 3:
            pClass = "Bard"
            slowText("You are a " + pClass)

            break
        elif choice == 4:
            pClass = "Cultist"
            slowText("You are a " + pClass)

            return pClass
        elif choice == 5:
            pClass = "Blacksmith"
            slowText("You are a " + pClass)

            return pClass
        elif choice == 6:
            #Tells user what each class does
            slowText("The Knight is the best at fighting monsters.")
            slowText("The Wizard can fight demons and monsters.")
            slowText("The Bard can play music to get money and appease ghosts.")
            slowText("The cultist can appease all those in the dark (monsters, ghosts, demons).")
            slowText("The blacksmith can make weapons so he doesn't always have to buy them.")

def moneySetup(pClass):
    if pClass == "Knight":
        money = 1000
        return money
    elif pClass == "Wizard":
        money = 800
        return money
    elif pClass == "Bard":
        money = 400
        return money
    elif pClass == "Cultist":
        money = 300
        return money
    elif pClass == "Blacksmith":
        money = 500
        return money


def nameSetup():
    """Sets the player name and party member names"""
    name = getInput("What is your name?", 2, 15)
    party.append(name)
    partySize = getNumber("How many are in your group? ", 8, 3)
    for i in range(1, partySize):
        name = getInput(str.format("What is party member {}'s name?", i+1), 2, 15)
        party.append(name)
    for i in range(0, len(party)):
      slowText(str.format("{} {}", i+1, party[i]))
    return party

def getInput(question, minLength, maxLength):
    while True:
        slowText(question)
        pInput = input()
        if len(pInput) >= minLength and len(pInput) <= maxLength:
            return pInput
        elif len(pInput) < minLength:
            slowText(str.format("Input must be at least {} characters.", minLength))
        elif len(pInput) > maxLength:
            slowText(str.format("Input must be shorter than {} characters.", maxLength+1))


def StartScreen():
    """ Displays the start menu with 3 options, start, learn, exit"""
    while True:
        oBanner = """THE UNNAMED ROUTE\n-------------------"""
        print(oBanner)
        startOptions = ["(1) Travel the Trail", " (2) Learn about the Trail", " (3) End"]
        startOptions[0:3]
        choice = getNumber(startOptions, len(startOptions)+1, 1)
        while True:
            if int(choice) == 1:#Play
                play()
                break
            elif int(choice) == 2:#Learn about trail
                learn()
                break
            elif int(choice) == 3:#quit
                slowText("Quit", 0.015)
                break
        if int(choice) == 3:#checks if the user quit before restarting the start screen
            break

def play():
    """Player chooses class, names of party, and game starts"""
    START_DATE = datetime.datetime(1300,3,1)
    current_date = START_DATE
    horseHp = 100
    totalMiles = 2000
    milesTraveled = 0
    money = 0
    food = 0
    arrows = 0
    clothes = 0
    parts = []

    horses = 0
    party = []
    weather = "good"
    hp = 100
    rations = "full"
    pace = "normal"


    pClass = charSetup()
    party = nameSetup()
    money = moneySetup(pClass)
    money, food, arrows, clothes, parts, horses = shop(money, food, arrows, clothes, parts, horses, len(party))
    while len(party) > 0 and totalMiles > 0:
        turn(hp, food, totalMiles, arrows, rations)
        if totalMiles <= 0:
            slowText("Congrats, you made it to the land of your desire!")
        elif len(party) <= 0:
            slowText("You and your friends are all dead... be more careful next time.")

def startMonth():
    pass

def shop(money, food, arrows, clothes, parts, horses, partySize):
    bill = 0
    inventory = []
    items = ["Horses", "Food", "Clothes", "Arrows", "Carriage Parts", "Check Out"]
    spentOnItems = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, bill]
    slowText("Before leaving CITYNAMEHERE you should buy some supplies for your journey.")
    slowText(str.format("You have {} gold pieces to spend on supplies.", money))
    slowText("Remember, you can buy supplies along the way.")
    slowText("Press Enter to Continue")
    input()
    slowText("Welcome to the NAMESHOPHERE shop!")
    slowText("Here are the things you can buy: ")
    while True:
        spentOnItems[len(spentOnItems)-1] = bill
        print()
        for i in range(len(items)-1):
            print(str.format("{}.        {:20}   {:.2f} Gold", i+1, items[i], spentOnItems[i]))
        print("6. Exit Shop")
        slowText(str.format("Total Bill so far:        {:.2f} Gold", bill), 0.02, 0)
        slowText(str.format("Total funds available:    {:.2f} Gold", money-bill), 0.02)
        choice = getNumber("What would you like to buy?", 7, 1)
        if choice == 1:
            bill -= spentOnItems[0]
            horses = 0
            spentOnItems[0] = 0.00
            slowText("For a group your size, I'd reccommend at least 3 horses")
            slowText("I charge 40 gold for a horse")
            answer = getNumber("How many horses do you want?", partySize+1, 0)
            cost = int(answer) * 40
            horses = answer
            bill += cost
            spentOnItems[0] = cost
        elif choice == 2:
            bill -= spentOnItems[1]
            food = 0
            spentOnItems[1] = 0.00
            slowText(str.format("""I reccommend you take at least 40 rations for each person in your party.
I see that you have {} party members. My price is 1 gold per ration.""", partySize))#Test for removing empty space
            answer = getNumber("How many rations of food do you want?", 50*partySize, 0)
            cost = int(answer)
            food = answer
            bill += cost
            spentOnItems[1] = cost
        elif choice == 3:
            bill -= spentOnItems[2]
            clothes = 0
            spentOnItems[2] = 0.00
            slowText("""You'll need warm clothing when your quest takes you to the mountains.
I recommend taking at least 2 sets of clothes per person. Each set is 10 gold.""")#Test for removing empty space
            answer = getNumber("How many sets of clothes do you want?", partySize*3, 0)
            cost = int(answer) * 10
            clothes = answer
            bill += cost
            spentOnItems[2] = cost
        elif choice == 4:
            bill -= spentOnItems[3]
            arrows = 0
            spentOnItems[3] = 0.00
            slowText("""I sell arrows in quivers of 20 arrows. Each quiver is 2 gold.""")
            answer = getNumber("How many quiver's do you want?", 150, 0)
            cost = int(answer) * 2
            arrows = answer
            bill += cost
            spentOnItems[3] = cost
        elif choice == 5:
                bill -= spentOnItems[4]
                partsBill = 0
                #parts[0] = 0
                #parts[1] = 0
                #parts[2] = 0
                spentOnItems[4] = 0.00
                slowText("It's a good idea to have a few spare parts for your carriage.")
                parts = ["carriage wheel", "carriage axle", "horse lead"]
                partsCost = [10, 10, 10, partsBill]
                while True:
                    partsCost[len(partsCost)-1] = partsBill
                    slowText("Here is a list of cart parts you can purchase :")
                    for i in range(len(parts)):
                        print(str.format("{}.    {:20}       {:.2f} gold", i+1, parts[i], partsCost[i]))
                    print("4.    Continue to Shop")
                    item = getNumber("what Item would you like to buy?", 5, 1)
                    if item == 1:
                        answer = getNumber("How many carrige wheels do you want?", 4, 0)
                        for i in range(answer):
                            inventory.append("Carriage Wheel")
                        partsBill += partsCost[0]*answer
                    elif item == 2:
                        answer = getNumber("How many carrige axels do you want?", 4, 0)
                        for i in range(answer):
                            inventory.append("Carrige Axle")
                        partsBill += partsCost[1]*answer
                    elif item == 3:
                        answer = getNumber("How many horse leads do you want?", 10, 0)
                        for i in range(answer) :
                            inventory.append("Horse Lead")
                        partsBill += partsCost[2]*answer
                    elif item == 4:
                        bill += partsBill
                        spentOnItems[4] = partsBill
                        break


        elif choice == 6:
            if bill <= money:
                money -= bill
                return money, food, arrows, clothes, inventory, horses
            else:
                slowText("You don't have that much money alter your shopping list. (Choice 1 will reset your money.)")

        else:
            slowText("Choose a valid option between 1 and 6")
            input()

        input()
def travel(weather, pace, hp):
    hours = 0
    mph = 0
    weatherMod = 0
    #hp
    if hp >= 80:
        hours = 8
    elif hp< 80 and hp >=55:
        hours = 4
    else:
        hours = 2
    #pace:
    if pace == "slow":
        mph = 1
    elif pace == "fast":
        mph = 4
    else:
        mph = 8
    #weather:
    if weather == good:
        weatherMod = 1
    elif weather == rain:
        weatherMod = 0.5
    else:
        weatherMod = 0
    miles = hours*mph*weatherMod
    return miles


def supplies():
    slowText(str.fromat("You have:\n {} gold",money))
    slowText(str.fromat("{} rations of food",food))
    slowText(str.fromat("{} pairs of clothes",clothes))
    slowText(str.fromat("{} horses",horses))
    slowText(str.fromat("{} arrows",arrows))


def pace(pace):
    pacer = getNumber("Pace (1 = normal, 2 = fast, 3 = slow): ", 3, 1)
    if pacer == 1:
        pace = "normal"
    elif pacer == 2:
        pace = "fast"
    elif pacer == 3:
        pace = "slow"
    return pacer
def hunt():
    success = False
    lostArrows = random.randint(-3, -10)
    num = random.randint(1,5)
    if num == 1 or num == 3:
        success = True
    else:
        success = False
    if success:
        animals = ["deer", "boar", "turkey", "pheasant", "squirrel", "bear"]
        hunted = random.choice(animals)
        if hunted == "bear":
            food = 200
            return food, lostArrows
        elif hunted == "deer":
            food = 100
            return food, lostArrows
        elif hunted == "boar":
            food = 60
            return food, lostArrows
        elif hunted == "turkey":
            food = 40
        elif hunted == "pheasant":
            food = 20
        else:
            food = 10
            return lostArrows, food
    else:
        return lostArrows

def rations(food):
    slowText("You currently have " + food + "pounds of food.")
    choice = getNumber("What should your rations be?\n(1 = full, 2= half, 3= bare bones) ", 3, 1)
    if choice == 1:
        rations = "full"
        return rations
    elif choice == 2:
        rations = "half"
        return rations
    else:
        rations = "bare bones"
        return rations


def rest(hp, rations):
    hpMod = 0.0
    restDays = getNumber("How many days do you want to rest? ", 10, 1)
    if rations == "full":
        hpMod = 2
    elif rations == "half":
        hpMod = 1
    else:
        hpMod = 0.5
    hpGain = 10*restDays*hpMod
    if hpGain+hp >= 100:
        hp = 100
    else:
        hp += hpGain
    return hp



def turn(hp, food, totalMiles, arrows, rations):
    weather = random.choice(["hot", "good", "fair", "poor", "windy", "rain", "blizzard"])
    mainChoice = getNumber("Would you like to:\n(1) Rest \n(2) Hunt \n(3) Set Pace \n(4) Check Supplies \n(5) Continue Travel \n(6) Set Rations", 6,1)

    if mainChoice == 1:
        hp = rest(hp)
    elif mainChoice == 2:
        if arrows == 0:
            slowText("You don't have any arrows. You can't hunt.")
            return
        lostArrows, newFood = hunt()
        food += newFood
        arrows += lostArrows
    elif mainChoice == 3:
        pace = pace(pace)
    elif mainChoice == 4:
        checkSupplies()
    elif mainChoice == 5:
        totalMiles = travel(weather, pace, hp)
    elif mainChoice == 6:
        rations = rations(food)

    if hp >= 80:
        hpCondition = "good"
    elif hp < 80 and hp >= 50:
        hpCondition = "fair"
    else:
        hpCondtition = "poor"



    if rations == "full":
        rationsMod = 2
    elif rations == "half":
        rationsMod = 1
    else:
        rationsMod = 0.5

    problem = random.choice(["lost", "snake bite", "sick", "horse died", "none", "none",
                             "none", "none","none", "none", "none", "none",
                             "none", "none", "none", "none"])

    if problem == "lost":
        lost = random.randint(1,7)
        person = random.choice(party)
        slowText(str.format("{0} got lost for {1} days.",person, lost))
        currentDate += datetime.timedelta(days = lost)
    if problem == "snake bite":
        hp -= 50
    if problem == "sick":
        hp -= 20
    if problem == "horse died":
        horse -= 1
        food += 50
        slowText("""One of your horses died. You now have more food.
Don't worry, you're not a horrible person if you eat a horse.""")

#Universal Variables
money = 0
food = 0
arrows = 0
clothes = 0
parts = []

horses = 0
party = []
#game startup
LogoScreen()
input()#stop to check def
StartScreen()
input()#stop to check def
