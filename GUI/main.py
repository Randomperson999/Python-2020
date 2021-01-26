# Caleb Keller
# 1/26/2021
# 1st-2nd

# ---|Text Boxes|---

from tkinter import *

class App(Frame):
    def __init__(self, master):
        self.usernames = ["[name]"]
        self.passwords = ["Passworld"]
        self.trys = 0
        super(App, self).__init__(master)
        self.grid()
        self.bg = "black"
        self.config(bg=self.bg)
        self.createWidgets()
    def createWidgets(self):
        self.lbl = Label(self, text="Enter Information", height=3, bg="black", fg="white")
        self.lbl.grid(row=0, column=0, columnspan=3, sticky=N)

        self.userLbl = Label(self, text="Please enter your username:", bg="black", fg="white")
        self.userLbl.grid(row=1, column=0, sticky=W)
        self.userTb = Entry(self)
        self.userTb.grid(row=1, column=1)

        self.passLbl = Label(self, text="Please enter your password:", bg="black", fg="white")
        self.passLbl.grid(row=2, column=0, sticky=W)
        self.passTb = Entry(self)
        self.passTb.grid(row=2, column=1)

        self.loginBttn = Button(self, text="Login", width=12, bg="grey")
        self.loginBttn.grid(row=3, column=1, rowspan=2, sticky=E)
        self.loginBttn["command"] = self.submit
        self.output = Text(self)
        self.output.config(bg="#d3d3d3")
        self.output.grid(row=5, columnspan=3)


    def submit(self):
        username = self.userTb.get()
        password = self.passTb.get()
        if username.lower() in self.usernames:
            if password in self.passwords:
                if self.trys <= 2:
                    message = "\n\n\tAccess Granted"
                    self.trys = 0
                else:
                    message = "\n\n\tAccount Locked"


            else:
                message = "\n\n\tIncorrect Password"
                self.trys += 1

        else:
            message = "\n\n\tIncorrect Username"
            self.trys += 1

        if self.trys > 3:
            message = "\n\n\tWii will fight you, you iMpOsTeR!"
        self.output.delete(0.0, END)
        self.output.insert(0.0, message)



def main():
    root = Tk()
    root.title("Password Entry")
    root.geometry("800x800")
    root.config(bg="black")
    root = App(root)
    root.mainloop()
main()

