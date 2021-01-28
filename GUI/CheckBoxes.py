#Caleb Keller
# 1/28/2021
# Check Boxes
from tkinter import *


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.bg = "blue"
        self.grid()
        self.config(bg=self.bg)
        self.createWidgets()

    def createWidgets(self):
        self.title = Label(self, text="|-----------Best Games-----------|", bg=self.bg)
        self.title.grid(column=0, row=0, rowspan=4, columnspan=3)
        self.question = Label(self, text="Select all that apply:", bg=self.bg)
        self.question.grid(column=0, row=4)

        self.lks_beat_sbr = BooleanVar()
        Checkbutton(self,
                    text="Beat Saber",
                    bg="blue",
                    variable = self.lks_beat_sbr,
                    command = self.update
                    ).grid(row=5, column=0, sticky=W)
        self.lks_link = BooleanVar()
        Checkbutton(self,
                    text="A Link to The Past",
                    bg="blue",
                    variable=self.lks_link,
                    command=self.update
                    ).grid(row=6, column=0, sticky=W)


        self.txt = Text(height=18, width=50, bg= "grey")
        self.txt.grid(column=0, row=8)
        self.worstFood = StringVar()
        self.worstFood.set(None)
        Radiobutton(self,
                    text="School Food",
                    value="School Food",
                    variable=self.worstFood,
                    command=self.update,
                    bg=self.bg
                    ).grid(column=0, row=7, sticky=W)
        Radiobutton(self,
                    text="School Food",
                    value="School Foods",
                    variable=self.worstFood,
                    command=self.update,
                    bg=self.bg
                    ).grid(column=0, row=8, sticky=W)
        Radiobutton(self,
                    text="School Food",
                    value="School's Food",
                    variable=self.worstFood,
                    command=self.update,
                    bg=self.bg
                    ).grid(column=0, row=9, sticky=W)

    def update(self):
        likes = ""
        if self.lks_beat_sbr.get():
            likes += "\n\tYou're a good person."
        if self.lks_link.get():
            likes += "\n\tThat's a classic."
        likes += "\n\tYour least favorite food is "+self.worstFood.get()
        self.txt.delete(0.0, END)
        self.txt.insert(0.0, likes)



def main():
    root = Tk()
    root.title("Games That Are Good")
    root.geometry("800x800")
    root.config(bg="blue")
    root = App(root)
    root.mainloop()
main()