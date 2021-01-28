#Caleb Keller
# 1/28/2021
# Tkinter Stuff
from tkinter import *

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.bg = "grey"
        self.config(bg=self.bg)
        self.grid
        self.createWidgets()

    def createWidgets(self):
        self.lbl = Label(self, text="")
        self.lbl.grid(column=0, row=0)

def main():
    root = Tk()
    root.title("GUI")
    root.geometry("800x800")
    root.config(bg="grey")
    root = App(root)
    root.mainloop()
main()