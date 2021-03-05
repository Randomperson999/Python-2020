# Mad Libs
# 2/17/2021
# Jadiah Jensen, Caleb Keller

from tkinter import *

HEIGHT = 300
WIDTH = 300
TITLE = "Mad Lib"
BACKGROUND = "Black"

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.config(bg="Black")
        self.grid()
        self.createWidgets()


    def createWidgets(self):
        self.partsList = []

        lbln1 = Label(self, text="Noun(Place)", bg="Black", fg="Red")
        lbln1.grid(row=0, column=0)
        noun1 = Entry(self, bg="Black", fg="Red")
        noun1.grid(row=0, column=1, columnspan=2)
        self.partsList.append(noun1)

        lbln2 = Label(self, text="Noun(Animal)", bg="Black", fg="Red")
        lbln2.grid(row=1, column=0)
        noun2 = Entry(self, bg="Black", fg="Red")
        noun2.grid(row=1, column=1, columnspan=2)
        self.partsList.append(noun2)

        lbla1 = Label(self, text="Adjective", bg="Black", fg="Red")
        lbla1.grid(row=2, column=0)
        adj1 = Entry(self, bg="Black", fg="Red")
        adj1.grid(row=2, column=1, columnspan=2)
        self.partsList.append(adj1)

        lblbP = Label(self, text="Noun(Body Part)", bg="Black", fg="Red")
        lblbP.grid(row=3, column=0)
        bodyPart = Entry(self, bg="Black", fg="Red")
        bodyPart.grid(row=3, column=1, columnspan=2)
        self.partsList.append(bodyPart)

        lblname = Label(self, text="Name", bg="Black", fg="Red")
        lblname.grid(row=4, column=0)
        name = Entry(self, bg="Black", fg="Red")
        name.grid(row=4, column=1, columnspan=2)
        self.partsList.append(name)

        lblplace = Label(self, text="Noun(Place)", bg="Black", fg="Red")
        lblplace.grid(row=5, column=0)
        place = Entry(self, bg="Black", fg="Red")
        place.grid(row=5, column=1, columnspan=2)
        self.partsList.append(place)

        lblv1 = Label(self, text="Verb", bg="Black", fg="Red")
        lblv1.grid(row=6, column=0)
        verb1 = Entry(self, bg="Black", fg="Red")
        verb1.grid(row=6, column=1, columnspan=2)
        self.partsList.append(verb1)

        lbln3 = Label(self, text="Noun", bg="Black", fg="Red")
        lbln3.grid(row=7, column=0)
        noun3 = Entry(self, bg="Black", fg="Red")
        noun3.grid(row=7, column=1, columnspan=2)
        self.partsList.append(noun3)

        lblv2 = Label(self, text="Verb", bg="Black", fg="Red")
        lblv2.grid(row=8, column=0)
        verb2 = Entry(self, bg="Black", fg="Red")
        verb2.grid(row=8, column=1, columnspan=2)
        self.partsList.append(verb2)

        lblv3 = Label(self, text="Verb", bg="Black", fg="Red")
        lblv3.grid(row=9, column=0)
        verb3 = Entry(self, bg="Black", fg="Red")
        verb3.grid(row=9, column=1, columnspan=2)
        self.partsList.append(verb3)

        start = Button(self, text="See Story", command = self.getStory, bg="Black", fg="Red")
        start.grid(row=10, column=1)


    def getStory(self):
        words = []

        for i in range(len(self.partsList)):
            value = self.partsList[i].get()
            words.append(value)
        story = str.format("""In the {0}, there was a {1} with a {2} {3}. The {1} gazed 
        deeply into {4}'s eyes filling him with fear. {4} knew it was the end for him. As {0} fell upon the 
        surface of the {6}, {4} began {7} quickly away from the {1}, hoping to escape his {8}. {4} fell dead 
        onto the floor and then
        {9}ed""", words[0], words[1], words[2], words[3], words[4], words[5],
                           words[6], words[7], words[8], words[9])
        print(story)
def main():
    root = Tk()
    root.geometry(str.format("{}x{}", WIDTH, HEIGHT))
    root.config(bg=BACKGROUND)
    root = App(root)
    root.mainloop()


main()

