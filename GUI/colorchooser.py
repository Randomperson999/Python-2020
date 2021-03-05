#Caleb Keller
# 1/28/2021
# Tkinter Stuff
from tkinter import *
from tkinter import colorchooser


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.bg = "grey"
        self.config(bg=self.bg)
        self.pack(fill=BOTH, expand=1)
        self.createWidgets()

    def createWidgets(self):
        self.btn = Button(self, text="Choose Color", command=self.onChoose)
        self.btn.place(x=30, y=30)
        self.frame = Frame(self, border=10, relief=RAISED, width=100, height=100)
        self.frame.place(x=160, y=30)

    def onChoose(self):
        (rgb, hx) = colorchooser.askcolor()
        self.frame.config(bg=hx)
        print(hx)


def main():
    root = Tk()
    root.title("Color Chooser")
    root.geometry("800x800")
    root.config(bg="grey")
    root = App(root)
    root.mainloop()


main()
