# Caleb Keller
# 2/11/2021
# Menu Systems
# Made by Mr. Broadbent

#imports
from tkinter import *
import os

HEIGHT = 800
WIDTH = 800
TITLE = "Menu Bars"
BACKGROUND = "black"
FONT = "San_Serif"


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.col = 0

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        menuBar = Menu(self.master)
        self.master.config(menu=menuBar)
        fileMenu = Menu(menuBar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Save", command=self.onSave)
        menuBar.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menuBar)
        editMenu.add_command(label="Create Frame", command=self.createFrame)
        editMenu.add_command(label="Destroy Frame", command=self.destroyFrame)
        menuBar.add_cascade(label="Edit", menu=editMenu)

        subMenu = Menu(fileMenu)
        subMenu.add_command(label="New Feed")
        subMenu.add_command(label="Bookmarks")
        subMenu.add_command(label="Mail")

        fileMenu.add_cascade(label="Import", menu=subMenu)
        fileMenu.add_separator()

    def onExit(self):
        self.quit()

    def onOpen(self):
        os.system("test.py")

    def onSave(self):
        pass

    def destroyFrame(self):
        self.frame1.destroy()

    def createFrame(self):
        self.frame1 = Frame(self, bg="red", width=250, height=250)
        self.frame1.grid(row=1, column=self.col)
        self.lbl1 = Label(self.frame1, text="testing")
        self.lbl1.pack(padx=20, pady=20, fill=BOTH, expand=1)
        self.lbl1["text"] = "change"
        self.col += 1


def main():
    root = Tk()
    root.geometry(str.format("{}x{}", WIDTH, HEIGHT))
    root.title(TITLE)
    root.config(bg=BACKGROUND)
    app = App(root)
    root.mainloop()

main()