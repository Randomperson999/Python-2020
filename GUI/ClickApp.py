# Caleb Keller
# 1/22/2021
# Clicker Counter
# Working with even handlers

# Imports
from tkinter import *

class App(Frame):
    """GUI application that counts button clicks. """
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.color = "white"
        self.total = 0
        self.colors = ["#FFFFFF","red", "blue", "green", "#000000"]
        self.colorIndex = 0
        self.createWidgets()

    def createWidgets(self):
        # Create all Widgets
        self.lbl1 = Label(self, text = "Total Clicks: ", bg=self.color)
        self.lbl2 = Label(self, text = str(self.total))
        self.bttnAdd = Button(self, text = " +  Click")
        self.bttnAdd.config(command = self.addToCount)
        self.bttnMin = Button(self, text = " -  Click")
        self.bttnMin["command"] = self.minFromCount
        self.bttnColor = Button(self, text = "Change Color", command = self.changeColor, width = 30, height = 9)

        # Add widgets to grid
        self.bttnColor.grid()
        self.lbl1.grid()
        self.lbl2.grid()
        self.bttnAdd.grid()
        self.bttnMin.grid()
        
    def addToCount(self):
        self.total += 1
        self.lbl2.config(text = str(self.total))
        self.changeLblColor()
        #print(self.total)
        
    def minFromCount(self):
        self.total -= 1
        if self.total < 0:
            self.total = 0
        self.lbl2.config(text = str(self.total))
        self.changeLblColor()
        #print(self.total)
        
    def changeColor(self):
        self.config(bg = self.colors[self.colorIndex])
        self.color=self.colors[self.colorIndex]
        if self.color == "#000000":
            self.lbl1.config(bg=self.color, fg= "white")
        else:
            self.lbl1.config(bg=self.color, fg="#000000")
        self.colorIndex += 1
        if self.colorIndex > 4:
            self.colorIndex = 0
    
    def  changeLblColor(self):
        if self.total < 150:
            self.lbl2["bg"] = "green"
        elif self.total >= 150 and self.total < 200:
            self.lbl2["bg"] = "yellow"
        else:
            self.lbl2["bg"] = "red"
        
def main():
    root = Tk()
    root.title("Click App")
    root.geometry("200x250")
    root.resizable(0,0)
    root.config(bg = "white")
    app = App(root)
    

    #Kick off main loop
    root.mainloop()
if __name__ =='__main__':
    main()
