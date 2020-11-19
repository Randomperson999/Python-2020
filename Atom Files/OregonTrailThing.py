#Caleb Keller
#REEEEEEEEEEEEEEEEEEEEEEEEEEEEE
import datetime
import random
START_DATE = datetime.datetime(1843,3,1)
current_date = START_DATE
hp = 100
horseHp = 100
totalMiles = 2000
milesTraveled = 0
food = 1000
rations = "full"
health = "good"
weather = "cold"
pace = "normal"
wagonHealth = 100

def turn(hp):
    weather = random.choice(["hot", "good", "fair", "poor", "windy", "rain", "blizzard"])
    if hp >=80:
        healthCondition = "good"
    elif hp < 80 and hp >= 50:
        healthCondition = "fair"
    else:
        healthCondtition = "poor"

    if rations == "full":
        rationsMod = 2
    elif rations == "half:
        rationsMod = 1
    else:
        rationsMod = 0.5
    num = random.randint(1, 100)
    if num >= 50 and num < 60:
        problem = random.choice(["lost", "snake bite", "sick", "horse died"])
    if problem == "lost":
        lost = random.randint(1, 7)
        lostOne = random.choice(party)
        slowText(str.format("{0} got lost for {1} days.", lostOne, lost))
        currentDate += datetime.timedelta(days = lost)
        food -= (len(party)*rationMod *lost)
    if problem == "sick":
        hp -= 20
    if problem == "snake bite":
        hp -= 50
    if problem == "horse died":
        horse -= 1
        food += 50
        slowText("""One of your horses died. You now have more food.
Don't worry, you're not a horrible person if you eat a horse.""")
    print("") #This will be ascii art so it needs to use the print statement
        
        
        
    
