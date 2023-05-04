from cell import Cell
from random import randrange
class Grid:
    grid = []
    xSize, ySize = 0, 0
    def __init__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize
        for i in range(xSize):
            self.grid.append([])
            for j in range(ySize):
                self.grid[i].append(Cell(False, False, 0, i, j))

    
    def __iter__(self):
        self.iterVal = -1
        return self
    
    def __next__(self):
        self.iterVal += 1
        if self.iterVal >= self.xSize:
            raise StopIteration
        else:
            return GridRow(self.grid[self.iterVal], self.ySize)
        
    def __len__(self):
        return len(self.grid)
    
    def __str__(self):
        retval = ""
        for i in self:
            for j in i:
                retval += str(j)
            retval += "\n"
        return retval
    
    def calcAllNumbers(self):
        for i in range(self.xSize):
            for j in range(self.ySize):
                self.grid[i][j].setNumber(self.getCellNumberCalc(i, j))
    
    
    def getCellNumberCalc(self, x, y):
        retval = 0
        for i, j in self.getNeighbors(x, y):
            retval += 1 if self.isBomb(i, j) else 0
        return retval
    
    def getNumber(self, x, y):
        return self.grid[x][y].getNumber()
    
    def isBomb(self, x, y):
        return self.grid[x][y].isBomb()
    
    def addBomb(self, x, y):
        self.grid[x][y].makeBomb()
    
    def addRandomBombs(self, numBombs):
        for i in range(0, numBombs):
            needBomb = True
            while needBomb:
                x, y = (randrange(self.xSize), randrange(self.ySize))
                print(x, y)
                if (not self.isBomb(x, y)):
                    self.addBomb(x, y)
                    needBomb = False


    def removeBomb(self, x, y):
        self.grid[x][y].changeBomb(False)

    def nonRecursiveOpen(self, x, y):
        self.grid[x][y].open()
        if self.grid[x][y].isBomb():
            return False
        return True
        

    def open(self, x, y):
        self.grid[x][y].open()
        if self.grid[x][y].isBomb():
            return False
        if self.grid[x][y].number == 0:
            for x, y in self.getNeighbors(x, y):
                if not self.grid[x][y].isOpened:
                    self.open(x, y)
        return True
    
    
    def getNeighbors(self, x, y):
        retval = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                print()
                if i >= 0 and i< self.xSize and j>=0 and j<self.ySize and not (i == x and j == y):
                    retval.append((i, j))
        
        return retval
    
class GridRow:
    row = []
    len = 0
    def __init__(self, row, len):
        self.row = row
        self.len = len
        self.iterVal = -1

    def __iter__(self):
        self.iterVal = -1
        return self
    
    def __next__(self):
        self.iterVal+= 1
        if self.iterVal>= len(self):
            raise StopIteration
        else:
            return self.row[self.iterVal]
        
    def __len__(self):
        return len(self.row)

