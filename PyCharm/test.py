import random
# v-Creates critter-v ^-imports-^
class Critter(object):
    """This is the class that defines what a critter is"""
    def __init__(self):
        self.health = 100
        self.hunger = 0
        self.height = 0
        self.weight = random.randint(2, 7)
        self.name = " "
        self.happy = 50
        self.isAlive = True
    #getters
    def getHunger(self):
        return self.hunger
    def getHealth(self):
        return self.health
    def getHeight(self):
        return self.height
    def getWeight(self):
        return self.weight
    def getHappy(self):
        return self.happy
    def getName(self):
        return self.name
    #setters
    def setName(self, name):
        if len(name) > 3:
            if "uck" not in name :
                self.name = name
            else:
                self.name = "[Name]"
                print("You can't do that...even if it's just duck.")
        self.name = name
    def setHeight(self, height):
        self.height = height
        if height < 5 and height > 1:
            self.height = height
    #intro
    def intro(self):
        print("Henlo, my name is "+self.getName)
    def hud(self):
        print(self.getName())
        health = self.getHealth
        if health > 80:
            print("Health: Great")
        elif health > 60:
            print("Health: Good")
        elif health > 50:
            print("Health: Fair")
        elif health == 0:
            self.die()
        else:
            print("Health: Poor")
        hunger = self.getHunger()
        if hunger > 40:
            print("Hunger: Starving")
        elif hunger > 20:
            print("Hunger: Hungry")
        elif hunger < 10:
            print("Hunger: Full")
        else:
            print("Hunger: Really Hungry")
        if hunger == 100:
            self.die
        if hunger == -100:
            self.die
        happy = self.getHappy()
        if happy == 100:
            print("Mood: Overjoyed")
        elif (happy < 100) and (happy > 80):
            print("Mood: Very Happy")
        elif happy >= 70:
            print("Mood: Happy")
        elif happy >= 50:
            print("Mood: Ok")
        elif happy >= 30:
            print("Mood: Bored")
        elif happy < 30:
            print("Mood: Depressed")
    def die(self):
        print("Your pet has died. You're a monster for letting it die.")
        self.health = 0
        self.isAlive = False


    #Feeds the critter
    def feed(self, food):
        if food == "pizza":
            self.hunger -= 7
        elif food == "cheese burger":
            self.hunger -= 13
        elif food == "steak":
            self.hunger -= 23
        elif food == "corn":
            self.hunger -= 3
        elif food == "cake":
            self.hunger -= 100
        else:
            self.hunger -= 5
    #Passes time
    def pass_time(self, hours):
        for i in range(hours):
            self.hunger += 2
            if self.hunger < 0:
                self.weight += 1
                self.happy += 10
            elif self.hunger < -30:
                self.health -= 10
            if self.hunger > 50:
                self.weight -= 1
                self.happy -= 10
                self.health -= 5
            self.happy -= 5
    #Heals and increases happiness
    def play(self, time):
        self.pass_time(self, time)
        self.happy += 10*time
        if self.happy > 100:
            self.happy = 100
        self.health += 10 * time
        if self.health > 100:
            self.health = 100





#main
def main():
    pet = Critter()
    name = input("What would you like to name your pet: ")
    pet.setName(name)
    height = int(input("How tall is your pet (2-5): "))
    pet.setHeight(height)
    pet.intro
    pet.hud
    while pet.isAlive:
        pet.pass_time(1)
        print("What do you want to do: \n")
        print("feed")
        print("play")
        print("nothing")
        response = input()
        if response == "feed":
            food = input("What would you like to feed your pet")
            pet.feed(food)
        if response == "play":
            time = int(input("How long will you play with your pet."))
            pet.play(time)
        pet.hud()
main()