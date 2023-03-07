class Cell:
    isBomb = False
    isOpened = False
    number = 0
    def __new__(self, isBomb, isOpened, number):
        self.isBomb = isBomb
        self.isOpened = isOpened
        self.number = number

    def changeBomb(self, isBomb):
        self.isBomb = isBomb
    
    def makeBomb(self):
        self.isBomb =True
    
    def isBomb(self):
        return self.isBomb

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