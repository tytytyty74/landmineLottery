from cell import Cell
class Grid:
    grid = []
    xSize, ySize = 0, 0
    def __new__(self, xSize, ySize):
        self.xSize = xSize
        self.ySize = ySize
        for i in range(xSize):
            self.grid.append([])
            for j in range(ySize):
                self.grid.append(Cell(False, False, 0))
    
    def addBomb(self, x, y):
        self.grid[x][y].makeBomb()

    def removeBomb(self, x, y):
        self.grid[x][y].changeBomb(False)

    def open(self, x, y):
        self.grid[x][y].open()
        if self.grid[x][y].isBomb():
            return False
        if self.grid[x][y].number == 0:
            for x, y in self.getNeighbors(x, y):
                self.open(x, y)
        return True
    
    
    def getNeighbors(self, x, y):
        retval = []
        for i in range(x-1, x+1):
            for j in range(y-1, y+1):
                if i > 0 and i< self.xSize and j>0 and j<self.xSize and (i != x and j != y):
                    retval.append((i, j))

        return retval