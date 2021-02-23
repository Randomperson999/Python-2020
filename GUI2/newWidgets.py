from tkinter import *
from tkinter.ttk import *
import tkinterStuff as tks
class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.bg = "grey"
        self.pack(fill = X)
        self.createWidgets()
    def createWidgets(self):
        self.listBox = Listbox(self)
        listItems =  ["1", "2e", "E", "I", "n"]
        for i in range(len(listItems)):
            self.listBox.insert(i,listItems[i])
        self.listBox.pack()
        self.submit = Button(self, text = "Try Me", command=self.changeValues)
        self.submit.pack(side=LEFT)
    def changeValues(self):
        pass
        
        

    
def main():
        root = Tk()
        root.title("GUI")
        root.config(bg = "grey")
        root = App(root)
        root.mainloop()

main()
