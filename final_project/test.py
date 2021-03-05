import main as m
from tkinter import *


def main():
    root = Tk()
    root.title("GUI")
    root.geometry("800x800")
    root.config(bg="grey")
    root = m.App(root)
    root.createLbl("test", 0, 0, "grey")
    root.mainloop()
main()
