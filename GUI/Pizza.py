#Caleb Keller
# 1/28/2021
# Tkinter Stuff
from tkinter import *

class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.bg = "black"
        self.fg = "white"
        self.grid()
        self.config(bg=self.bg)
        self.createWidgets()

    def createWidgets(self):
        Label(self,
              text="Pizza Ordering Thing",
              bg=self.bg,
              fg=self.fg
              ).grid(row=0,
                     rowspan=3,
                     column=0,
                     columnspan=3)
        Label(self,
              text="What sauce? :\n",
              bg=self.bg,
              fg=self.fg,
              command=self.update
              ).grid(row=3,
                     column=0,
                     columnspan=3)
        Radiobutton(self,
                    text="Tomato",
                    bg=self.bg,
                    fg=self.fg,
                    command=self.update
                    ).grid(row=4,
                           column=0,
                           columnspan=1)
        Radiobutton(self,
                    text="Buffalo",
                    bg=self.bg,
                    fg=self.fg,
                    command=self.update
                    ).grid(row=5,
                           column=0,
                           columnspan=1)
        Radiobutton(self,
                    text="Garlic Parmesan",
                    bg=self.bg,
                    fg=self.fg,
                    command=self.update
                    ).grid(row=6,
                           column=0,
                           columnspan=1)
        Radiobutton(self,
                    text="Garlic Parmesan",
                    bg=self.bg,
                    fg=self.fg,
                    command=self.update
                    ).grid(row=6,
                           column=0,
                           columnspan=1)
        Radiobutton(self,
                    text="pǝsɹnƆ",
                    bg=self.bg,
                    fg=self.fg,
                    command=self.cursed
                    ).grid(row=6,
                           column=0,
                           columnspan=1)
    def update(self):
        order = ""
    def cursed(self):
        pass


def main():
    root = Tk()
    root.title("GUI")
    root.geometry("800x800")
    root.config(bg="black")
    root = App(root)
    root.mainloop()
main()