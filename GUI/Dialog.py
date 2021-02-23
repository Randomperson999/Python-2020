#Caleb Keller
# 1/28/2021
# Tkinter Stuff
from tkinter import *
from tkinter import messagebox as mb
class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.bg = "grey"
        self.config(bg=self.bg)
        self.pack(fill=BOTH)
        self.createWidgets()

    def createWidgets(self):
        error = Button(self, text="Error", command=self.onError)
        error.grid(padx=5, pady=5)
        warning = Button(self, text="Warning", command=self.onWarn)
        warning.grid(row=1, column=0)
        question = Button(self, text="Question", command=self.onQuest)
        question.grid(row=0, column=1)
        inform = Button(self, text="Information", command=self.onInfo)
        inform.grid(row=1, column=1)

    def onError(self):
        mb.showerror("Error", "Could not open File")

    def onWarn(self):
        mb.showwarning("Warning", "Thou hast awakened him")

    def onQuest(self):
        result = mb.askquestion("Question", "Are you sure you want to quit?")
        if result == "yes":
            print("YOU")
        else:
            print("W O R D S")



    def onInfo(self):
        mb.showinfo("Info", "Download Complete")

def main():
    root = Tk()
    root.title("GUI")
    root.geometry("800x800")
    root.config(bg="grey")
    root = App(root)
    root.mainloop()
main()