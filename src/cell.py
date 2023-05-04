import pygame

grid_size = 32
border = 16
top_border = 100
game_width = 10
game_height = 10
class Cell:
    bomb = False
    isOpened = False
    flag = False
    number = 0
    clicked = False
    x= 0
    y = 0

    
    def __init__(self, bomb, isOpened, number, x, y):
        self.bomb = bomb
        self.isOpened = isOpened
        self.number = number
        self.x = x
        self.y = y
        self.rect = pygame.Rect(border + self.x * grid_size, top_border + self.y * grid_size, grid_size,
                                grid_size)
    def __str__(self):
        return "["+ ("X"if self.isBomb() else str(self.number))+ "]"
    

    def changeBomb(self, bomb):
        self.bomb = bomb
    
    def makeBomb(self):
        self.bomb =True
    
    def isBomb(self):
        return self.bomb

    def isOpened(self):
        return self.isOpened
    
    def open(self):
        self.isOpened = True

    def close(self):
        self.isOpened = False

    def getNumber(self):
        return self.number
    
    def setNumber(self, n):
        self.number = n

    def setFlag(self, bool):
        self.flag = flag