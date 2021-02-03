# Caleb Keller
# 2/3/2021
# Pictures In Tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinterStuff as tks
class Main():
    def __init__(self):
        self.index

    def changeImage(self):
        self.index = 0
        self.index += 1
    def createWidgets(self, root):
        root.createWidget("lbl", "My Favorite Pics!", False)
        logo1 = root.createWidget("img", None, False, 30, 40)
        logo2 = root.createWidget("img", None, False, 250, 40, 0, 0, None, "wood")
        logo3 = root.createWidget("img", None, False, 470, 40, 0, 0, None, "rock")
        imgList = [logo1, logo2, logo3]
        change = root.createWidget("bttn", "Change Image", False, 300, 250, 0, 0, self.changeImage)
    def main(self, width, height):
        root = Tk()
        root.title("Images")
        root.geometry(str(width)+"x"+str(height))
        root.config(bg="grey")
        root = tks.App(root)
        self.createWidgets(root)
        root.mainloop()


Main.main(Main, 800, 800)



