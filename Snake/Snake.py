# Caleb Keller
# Snake Game
# 2/19/2021

#imports

from tkinter import *
from PIL import ImageTk, Image
import random
import sys

# Classes
class Cons:
    BOARD_WIDTH = 500
    BOARD_HEIGHT = 500
    DELAY = 100
    DOT_SIZE = 10
    MAX_RAND_POS = 27

class Board(Canvas):

    def __init__(self):
        super(Board, self).__init__(width=Cons.BOARD_WIDTH,
                                    height=Cons.BOARD_HEIGHT,
                                    background="black", highlightthickness = 0)
        self.initGame()
        self.pack()
        
    def initGame(self):
        """initializes game"""
        self.inGame = True
        self.dots = 3
        self.score = 0

        # variables used to move snake object
        self.moveX = Cons.DOT_SIZE
        self.moveY = 0

        # starting apple coordinates
        self.appleX = 100
        self.appleY = 190

        # load images
        self.loadImages()
        # create Game objects
        self.createObjects()
        # place apple on screen
        self.locateApple()
        # Check if key is pressed
        self.bind_all("<Key>", self.onKeyPressed)
        self.after(Cons.DELAY, self.onTimer)
        
        
    def onTimer(self):
        '''creates a game cycle each timer event'''
        self.drawScore()
        self.checkCollision()
        if self.inGame == True:
            self.checkAppleCollision()
            self.moveSnake()
            self.after(Cons.DELAY, self.onTimer)
        else:
            self.gameOver()
    def   checkAppleCollision(self):
        pass
    
    def gameOver(self):
        pass
    
    def checkCollision(self):
        pass
    
    def drawScore(self):
        pass
    
    def moveSnake(self):
        pass
    
    def onKeyPressed(self, e):
        """controls direction variables with cursor keys"""
        key = e.keysym
        LEFT_CURSOR_KEY = "Left"
        RIGHT_CURSOR_KEY = "Right"
        UP_CURSOR_KEY = "Up"
        DOWN_CURSOR_KEY = "Down"
        if key == LEFT_CURSOR_KEY and self.moveX <= 0:
            self.moveX = -Cons.DOT_SIZE
            self.moveY= 0
        if key == RIGHT_CURSOR_KEY and self.moveX >= 0:
            self.moveX = Cons.DOT_SIZE
            self.moveY= 0
        if key == UP_CURSOR_KEY and self.moveY <= 0:
            self.moveX = 0
            self.moveY= -Cons.DOT_SIZE
        if key == DOWN_CURSOR_KEY and self.moveY >=0:
            self.moveX = 0
            self.moveY= Cons.DOT_SIZE
        
    def loadImages(self):
        """load images from the disk"""
        try:
            self.ibody = Image.open("imgs/Body.png")
            self.ihead = Image.open("imgs/Head.png")
            self.iapple = Image.open("imgs/Apple.png")
            self.body = ImageTk.PhotoImage(self.ibody)
            self.head = ImageTk.PhotoImage(self.ihead)
            self.apple = ImageTk.PhotoImage(self.iapple)

        except IOError as e:
            print(e)
            sys.exit(1)
    def createObjects(self):
        """creates objects on Canvas"""
        self.create_text(30, 10, text="Score {0}".format(self.score),
                         tag="score", fill = "white")
        self.create_image(self.appleX, self.appleY, image = self.apple,
                          anchor = NW, tag="apple")
        self.create_image(50, 50, image = self.head,
                          anchor = NW, tag="head")
        self.create_image(30, 50, image = self.body,
                          anchor = NW, tag="body")
        self.create_image(40, 50, image = self.body,
                          anchor = NW, tag="body")
        
        
    def locateApple(self):
        """places the apple object on Canvas"""
        apple=self.find_withtag("apple")
        self.delete(apple[0])
        r = random.randint(0, Cons.MAX_RAND_POS)
        self.appleX = r * Cons.DOT_SIZE
        r = random.randint(0, Cons.MAX_RAND_POS)
        self.appleX =  r * Cons.DOT_SIZE

        self.create_image(self.appleX, self.appleY, anchor=NW,
                          image=self.apple, tag ="apple")

class Snake(Frame):
    def __init__(self, master):
        super(Snake, self).__init__(master)
        self.master.title("Snake Ripoff")
        self.board = Board()
        self.pack()

def main():
    root = Tk()
    snake = Snake(root)
    root.mainloop()

main()
                
    
