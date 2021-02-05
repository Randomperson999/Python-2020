#Caleb Keller
# 1/28/2021
# Tkinter Stuff
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
HEIGHT = 800
WIDTH = 800
class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.bg = "grey"
        self.config(bg=self.bg)
        self.grid
        self.pack(fill=BOTH, expand=1)
        self.createWidgets()

    def createWidgets(self):
        pass
    def createWidget(self, type, txt="", isGrid=True, x1= 10, y1= 10, r=0, c=0, cmmd = None, imgA="nickcage", bg="white"):
        if type == "lbl":
            self.texts(type, txt, isGrid, x1, y1, r, c)
        elif type == "txt":
            self.texts(type, txt, isGrid, x1, y1, r, c)
        elif type == "entry":
            self.texts(type, txt, isGrid, x1, y1, r, c)
#      elif type == "bttn":
##          if isGrid == True:
##                Button(text=txt,
##                      bg=self.bg).grid(row=r,
##                                       column=c)
##            else:
##                Button(text=txt,
##                      bg=self.bg,
##                       command=cmmd).place(x=x1,
##                                        y=y1)
##        elif type == "rbttn":
##            if isGrid == True:
##                Radiobutton(text=txt,
##                     bg=self.bg,
##                            command=cmmd).grid(row=r,
##                                      column=c)
##            else:
##                Radiobutton(text=txt,
##                     bg=self.bg,
##                            command=cmmd).place(x=x1,
##                                       y=y1)
##        elif type == "cbttn":
##            if isGrid == True:
##                Checkbutton(text=txt,
##                     bg=self.bg).grid(row=r,
##                                      column=c)
##            else:
##                Checkbutton(text=txt,
##                     bg=self.bg,
##                            command=cmmd).place(x=x1,
##                                       y=y1)
        elif type == "list":
            if isGrid == True:
                Listbox(text=txt,
                     bg=self.bg).grid(row=r,
                                      column=c)
            else:
                Listbox(text=txt,
                     bg=self.bg).place(x=x1,
                                       y=y1)
        elif type == "img":
            try:
                img = Image.open(imgA+".png")
                logo1 = ImageTk.PhotoImage(img)
                self.imglbl1 = Label(self, image=logo1)
                self.imglbl1.image = logo1
                self.imglbl1.place(x=x1, y=y1)
            except:
                img2 = Image.open(imgA+".jpg")
                logo2 = ImageTk.PhotoImage(img2)
                self.imglbl2 = Label(self, image=logo2)
                self.imglbl2.image = logo2
                self.imglbl2.place(x=x1, y=y1)
        elif type == "bttn" or type == "rbbtn" or type == "cbbtn":
            bttns(type, txt, isGrid, x1, y1, r, c, cmmd)
        elif type == "cmbx":
            itemsList = [1, 2, 3, 4, 5, "hello"]
            self.combobox = Combobox(self,
                                     values= itemsList)
            self.combobox.current(3)
            self.combobox.pack(side=LEFT)
    # Widgets:
    def texts(self, type, txt, isGrid, x1, y1, r, c):
        if type == "lbl":
            if isGrid == True:
                Label(text=txt,
                      bg=self.bg).grid(row=r,
                                       column=c)
            else:
                Label(text=txt,
                      bg=self.bg).place(x=x1,
                                        y=y1)
        elif type == "txt":
            if isGrid == True:
                Text(text=txt,
                      bg=self.bg).grid(row=r,
                                       column=c)
            else:
                Text(text=txt,
                      bg=self.bg).place(x=x1,
                                        y=y1)
        elif type == "entry":
            if isGrid == True:
                Entry(text=txt,
                     bg=bg).grid(row=r,
                                      column=c)
            else:
                Entry(text=txt,
                     bg=bg).place(x=x1,
                                       y=y1)
        
            
    def bttns(self, type, txt="", isGrid=True, x1=10, y1=10, r=0, c=0, cmmd=None):
        if type == "bttn":
            if isGrid == True:
                Button(text=txt,
                      bg=self.bg).grid(row=r,
                                       column=c)
            else:
                Button(text=txt,
                      bg=self.bg,
                       command=cmmd).place(x=x1,
                                        y=y1)
        elif type == "rbttn":
            if isGrid == True:
                Radiobutton(text=txt,
                     bg=self.bg,
                            command=cmmd).grid(row=r,
                                      column=c)
            else:
                Radiobutton(text=txt,
                     bg=self.bg,
                            command=cmmd).place(x=x1,
                                       y=y1)
        elif type == "cbttn":
            if isGrid == True:
                Checkbutton(text=txt,
                     bg=self.bg).grid(row=r,
                                      column=c)
            else:
                Checkbutton(text=txt,
                     bg=self.bg,
                            command=cmmd).place(x=x1,
                                       y=y1)

def main(width, height):
    root = Tk()
    root.title("GUI")
    root.geometry(str(width)+"x"+str(height))
    root.config()
    root = App(root)
    root.mainloop()
