# Caleb Keller
# 1/20/2020
# Class GUI
from tkinter import *
import tkinter.font as tkFont

class Application(Frame):
    """A GUI app with three buttons"""

    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid
        self.createWidgets()
        self.clicks = 0
    def createWidgets(self):
        self.tclbl = Label(self,text = "Total Clicks: ")
        self.numClicks = Label(self, text = str(self.clicks))

        self.addbttn = Button(self, text = "+ to Clicks", bg = "gray")
        self.minbttn = Button(self, text="  - Clicks", bg="gray")

        self.colorbttn = Button(self, text = "Change background color")

        self.tclbl.grid()
        self.numClicks.grid()
        self.addbttn.grid()
        self.minbttn.grid()
        self.colorbttn.grid()



root = Tk()
root.title("Caleb's GUI")
root.geometry("720x720")
# color blue
root.configure(bg="#0000FF")

root.mainloop()