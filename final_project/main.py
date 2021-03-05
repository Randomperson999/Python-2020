# Caleb Keller, Jadiah Jensen
# 2/9/2021-2//2021
# Sample GUI

# Imports
from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.bg = "grey"
        self.config(bg=self.bg)
        self.grid
        self.createWidgets()

    def createWidgets(self):
        x=Frame(self)

    def createLbl(self, txt, r, c, bg="white"):
        Label(text=txt,
              bg=bg).grid(row=r,
                          column=c)

    def createTxt(self, txt, r, c, bg="white"):
        Text(self,
             text=txt,
             bg=bg).grid(row=r,
                         column=c)

    def createEntry(self, r, c, bg="white"):
        Entry(self,
              bg=bg).grid(row=r,
                          column=c)

    def createBttn(self, txt, r, c, cmmd, bg="white"):
        Button(text=txt,
               bg=bg,
               command=cmmd).grid(row=r,
                                  column=c)

    def create_cBttn(self, txt, r, c, cmmd, bg="white"):
        Checkbutton(text=txt,
                    bg=self.bg,
                    command=cmmd).grid(row=r,
                                       column=c)

    def create_rBttn(self, txt, r, c, cmmd, bg="white"):
        Radiobutton(text=txt,
                    bg=bg,
                    command=cmmd).grid(row=r,
                                       column=c)

    def createList(self, txt, r, c, cmmd, bg="white"):
        Listbox(text=txt,
                bg=bg,
                command=cmmd).grid(row=r,
                                   column=c)

# You do not need to call this when importing the file;
# just use 'main.App' instead of 'App' in that file.
def main():
    root = Tk()
    root.title("GUI")
    root.geometry("800x800")
    root.config(bg="grey")
    root = App(root)
    root.mainloop()
