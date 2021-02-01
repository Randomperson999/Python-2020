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
        self.order = StringVar()
        self.order.set(None)
        # Information
        self.createWidget("mlbl", 0, 0, 1, 3, "Information", N)
        self.createWidget("lbl", 4, 0, 1, 1, "Name: ")
        self.createWidget("lbl", 5, 0, 1, 1, "Address: ")
        self.createWidget("lbl", 6, 0, 1, 1, "Phone Number: ")
        self.createWidget("entry", 4, 1, 1, 1)
        self.createWidget("entry", 5, 1, 1, 1)
        self.createWidget("entry", 6, 1, 1, 1)

        # # Sauce
        # Label(self,
        #       text="Sauce",
        #       borderwidth=2,
        #       relief="sunken",
        #       bg="grey",
        #       ).grid(row=6,
        #              column=0,
        #              columnspan=3)
        # Radiobutton(self,
        #             text="Tomato",
        #             value="Tomato",
        #             bg=self.bg,
        #             fg=self.fg,
        #             variable=self.order,
        #             command=self.update
        #             ).grid(row=7,
        #                    column=0,
        #                    columnspan=1)
        # Radiobutton(self,
        #             text="Buffalo",
        #             value="Buffalo",
        #             bg=self.bg,
        #             fg=self.fg,
        #             variable=self.order,
        #             command=self.update
        #             ).grid(row=8,
        #                    column=0,
        #                    columnspan=1)
        # Radiobutton(self,
        #             text="Garlic Parmesan",
        #             value="Garlic Parmesan",
        #             bg=self.bg,
        #             fg=self.fg,
        #             variable=self.order,
        #             command=self.update
        #             ).grid(row=9,
        #                    column=0,
        #                    columnspan=1)
        # Radiobutton(self,
        #             text="Garlic Ranch",
        #             value="Garlic Ranch",
        #             bg=self.bg,
        #             fg=self.fg,
        #             variable=self.order,
        #             command=self.update
        #             ).grid(row=10,
        #                    column=0,
        #                    columnspan=1)
        # Radiobutton(self,
        #             text="pǝsɹnƆ",
        #             value="pǝsɹnƆ",
        #             bg=self.bg,
        #             fg=self.fg,
        #             variable=self.order,
        #             command=self.cursed
        #             ).grid(row=11,
        #                    column=0,
        #                    columnspan=1)
    def createWidget(self, widget, r, c, rsp=1, clmsp=1, txt="", stky=N, call=None, wdth=12,hght=1):
        # print(str.format("{0}, {1}, {2}, {3}, {4}, {5}", widget, r, c, rsp, clmsp, txt))
        if widget == "lbl":
            Label(self,
                  text=txt,
                  bg=self.bg,
                  fg=self.fg,
                  ).grid(row=r,
                         column=c,
                         columnspan=clmsp)
        elif widget == "mlbl":
            Label(self,
                  text=txt,
                  borderwidth=2,
                  relief="sunken",
                  bg="grey",
                  width=wdth
                  ).grid(row=r,
                         rowspan=rsp,
                         column=c,
                         columnspan=clmsp,
                         padx=10,
                         pady=10,
                         sticky=N)
        elif widget == "entry":
            Entry(self,
                  bg="grey",
                  ).grid(row=r,
                         column=c,
                         sticky=E)
        elif widget == "txt":
            pass
        elif widget == "cb":
            pass
        elif widget == "rb":
            pass

    def update(self):
        order = []

    def cursed(self):
        pass


def main():
    root = Tk()
    root.title("Pizza Ordering Thing")
    root.geometry("800x800")
    root.config(bg="black")
    root = App(root)
    root.mainloop()


main()
