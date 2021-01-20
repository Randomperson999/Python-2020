# Simple GUI
# Demonstrates creating a window
from tkinter import *
import tkinter.font as tkFont
# Create basic window
root = Tk()
root.title("Caleb's GUI")
root.geometry("720x720")
# color blue
root.configure(bg="#0000FF")
# Create Frame 1 to place widgets on
app = Frame(root,bg = "#0000A0")
app.grid()

# create label
fontStyle = tkFont.Font(family="Great Vibes", size=24, weight = "bold", underline = 0)
lbl = Label(app, text="Stuff:                    \n",bg = "#0000A0", fg = "#000000", font = fontStyle)

lbl.grid()

# Create Buttons
bttn1 = Button(app, text = "REEEEEEEEE", bg = "gray")
bttn1.grid()
bttn2 = Button(app)
bttn2.grid()
for i in range(5):
    x = Button(app)
    x["text"] = "Button "+str(i+1)
    x["bg"] = "gray"
    x.grid()
bttn2.config(text = "E E E EEEE",bg = "gray")
# Frame 2
app2 = Frame(root, width = 400, height = 400, bg="red")
app2.grid()
for i in range(7):
    y = Button(app2, text = "Button"+str(i), bg = "gray")
    y.grid()
app2.configure(width = 400, height = 400, bg="red")

# Kick off window's event loop
root.mainloop()
