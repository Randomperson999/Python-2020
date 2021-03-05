#Caleb Keller
# 1/28/2021
# Tkinter Stuff
from tkinter import *
from tkinter import filedialog as fd


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.bg = "grey"
        self.config(bg=self.bg)
        self.pack(fill=BOTH, expand=1)
        self.createWidgets()

    def createWidgets(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        menubar.add_cascade(label="File", menu=fileMenu)
        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def onOpen(self):
        ftypes = [("Python file", "*.py"), ("All files", "*")]
        dlg = fd.Open(self, filetypes=ftypes)
        f1 = dlg.show()
        if f1 != " ":
            text = self.readFile(f1)
            self.txt.insert(END, text)
    def readFile(self, filename):
        with open(filename, "r") as f:
            text = f.read()
        return text

def main():
    root = Tk()
    root.title("GUI")
    root.geometry("800x800")
    root.config(bg="grey")
    root = App(root)
    root.mainloop()
main()