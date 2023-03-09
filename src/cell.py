class Cell:
    bomb = False
    isOpened = False
    number = 0
    def __init__(self, bomb, isOpened, number):
        self.bomb = bomb
        self.isOpened = isOpened
        self.number = number
    def __str__(self):
        return "["+ ("X"if self.isBomb() else " ")+ "]"
    

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

    def number(self):
        return self.number
    
    def setNumber(self, n):
        self.number = n