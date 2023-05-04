import pygame
from random import randrange
import random

# resources 
spr_mine = pygame.image.load("resources/mine.png")
spr_mineClicked = pygame.image.load("resources/mineClicked.png")
spr_mineFalse = pygame.image.load("resources/mineFalse.png")
spr_emptyGrid = pygame.image.load("resources/empty.png")
spr_flag = pygame.image.load("resources/flag.png")
spr_grid = pygame.image.load("resources/Grid.png")
spr_grid1 = pygame.image.load("resources/grid1.png")
spr_grid2 = pygame.image.load("resources/grid2.png")
spr_grid3 = pygame.image.load("resources/grid3.png")
spr_grid4 = pygame.image.load("resources/grid4.png")
spr_grid5 = pygame.image.load("resources/grid5.png")
spr_grid6 = pygame.image.load("resources/grid6.png")
spr_grid7 = pygame.image.load("resources/grid7.png")
spr_grid8 = pygame.image.load("resources/grid8.png")

# grid setup stuff
# x = Grid(16, 16, "false")
grid_size = 32
border = 16
top_border = 100
game_width = 10
game_height = 10

# pygame setup stuff
pygame.init()
screen_yOffSet = 100
screen_xOffSet = 100
screen_width = 16 * 25 * 2 + screen_xOffSet
screen_height = 16 * 25 + 100 + screen_yOffSet
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('LandMineLottery')
clock = pygame.time.Clock()
timer = pygame.time.Clock()  # timer

# the grid
class Grid:
    grid = []
    xSize, ySize = 0, 0

    def __init__(self, type, xGrid, yGrid):
        # original init
        xSize, ySize = 16, 16
        self.xSize = xSize
        self.ySize = ySize
        for i in range(xSize):
            self.grid.append([])
            for j in range(ySize):
                self.grid[i].append(Cell(False, False, 0))
        # updated init
        self.xGrid = xGrid  # X pos of grid
        self.yGrid = yGrid  # Y pos of grid
        self.clicked = False  # Boolean var to check if the grid has been clicked
        self.mineClicked = False  # Bool var to check if the grid is clicked and its a mine
        self.mineFalse = False  # Bool var to check if the player flagged the wrong grid
        self.flag = False  # Bool var to check if player flagged the grid

        # Create rectObject to handle drawing and collisions
        self.rect = pygame.Rect(border + self.xGrid * grid_size, top_border + self.yGrid * grid_size, grid_size,
                                grid_size)
        self.val = type

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
                self.open(x, y)
        return True

    def getNeighbors(self, x, y):
        retval = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                print()
                if i >= 0 and i < self.xSize and j >= 0 and j < self.ySize and not (i == x and j == y):
                    retval.append((i, j))

        return retval

    def revealGrid(self):
        self.clicked = True
        # Auto reveal if it's a 0
        if self.val == 0:
            for x in range(-1, 2):
                if self.xGrid + x >= 0 and self.xGrid + x < game_width:
                    for y in range(-1, 2):
                        if self.yGrid + y >= 0 and self.yGrid + y < game_height:
                            if not grid[self.yGrid + y][self.xGrid + x].clicked:
                                grid[self.yGrid + y][self.xGrid + x].revealGrid()
        elif self.val == -1:
            # Auto reveal all mines if it's a mine
            for m in mines:
                if not grid[m[1]][m[0]].clicked:
                    grid[m[1]][m[0]].revealGrid()

    # updates after all grids are generated
    def updateValue(self):
        if self.val != -1:
            for x in range(-1, 2):
                if self.xGrid + x >= 0 and self.xGrid + x < game_width:
                    for y in range(-1, 2):
                        if self.yGrid + y >= 0 and self.yGrid + y < game_height:
                            if grid[self.yGrid + y][self.xGrid + x].val == -1:
                                self.val += 1

    def drawGrid(self, side = "left"):
        # Draw the grid according to bool variables and value of grid
        if self.mineFalse:
            screen.blit(spr_mineFalse, self.rect)
        else:
            if self.clicked:
                if self.val == -1:
                    if self.mineClicked:
                        screen.blit(spr_mineClicked, self.rect)
                    else:
                        screen.blit(spr_mine, self.rect)
                else:
                    if self.val == 0:
                        screen.blit(spr_emptyGrid, self.rect)
                    elif self.val == 1:
                        screen.blit(spr_grid1, self.rect)
                    elif self.val == 2:
                        screen.blit(spr_grid2, self.rect)
                    elif self.val == 3:
                        screen.blit(spr_grid3, self.rect)
                    elif self.val == 4:
                        screen.blit(spr_grid4, self.rect)
                    elif self.val == 5:
                        screen.blit(spr_grid5, self.rect)
                    elif self.val == 6:
                        screen.blit(spr_grid6, self.rect)
                    elif self.val == 7:
                        screen.blit(spr_grid7, self.rect)
                    elif self.val == 8:
                        screen.blit(spr_grid8, self.rect)

            else:
                if self.flag:
                    screen.blit(spr_flag, self.rect)
                else:
                    screen.blit(spr_grid, self.rect)


# grid row
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
        self.iterVal += 1
        if self.iterVal >= len(self):
            raise StopIteration
        else:
            return self.row[self.iterVal]

    def __len__(self):
        return len(self.row)


# a cell
class Cell:
    bomb = False
    isOpened = False
    number = 0

    def __init__(self, bomb, isOpened, number):
        self.bomb = bomb
        self.isOpened = isOpened
        self.number = number

    def __str__(self):
        return "[" + ("X" if self.isBomb() else str(self.number)) + "]"

    def changeBomb(self, bomb):
        self.bomb = bomb

    def makeBomb(self):
        self.bomb = True

    def isBomb(self):
        return self.bomb

    # def isOpened(self):
    #     return self.isOpened

    def open(self):
        self.isOpened = True

    def close(self):
        self.isOpened = False

    def getNumber(self):
        return self.number

    def setNumber(self, n):
        self.number = n


# draw texts in center of screen
def drawText(txt, s, yOff=0):
    screen_text = pygame.font.SysFont("Calibri", s, True).render(txt, True, (0, 0, 0))
    rect = screen_text.get_rect()
    rect.center = (game_width / 2, game_height / 2)
    screen.blit(screen_text, rect)


# actual game
def gameInSession():
    # init
    grid_color = (128, 128, 128)
    bg_color = (192, 192, 192)
    gameState = "Playing"
    mineLeft = 9  # Number of mine left
    global grid
    grid = []
    global mines
    time = 0  # Set time to 0
    white = (255, 255, 255)

    # title screen
    # test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
    # score_message_surf = test_font.render(f'LandmineLottery - {gameState}', False, (111, 196, 169))
    # score_message_rect = score_message_surf.get_rect(center=(screen_width / 2, screen_yOffSet - 5))
    # screen.blit(score_message_surf, score_message_rect)

    # Generating mines
    mines = [[random.randrange(0, game_width),
              random.randrange(0, game_height)]]

    for c in range(mineLeft - 1):
        pos = [random.randrange(0, game_width),
               random.randrange(0, game_height)]
        same = True
        while same:
            for i in range(len(mines)):
                if pos == mines[i]:
                    pos = [random.randrange(0, game_width), random.randrange(0, game_height)]
                    break
                if i == len(mines) - 1:
                    same = False
        mines.append(pos)

    # drawing first player's entire grid
    for j in range(game_height):
        line = []
        for i in range(game_width):
            if [i, j] in mines:
                line.append(Grid(xGrid=i, yGrid=j, type=-1))
            else:
                line.append(Grid(xGrid=i, yGrid=j, type=0))
        grid.append(line)

    # update the first player's of the grid
    for i in grid:
        for j in i:
            j.updateValue()

    # game loop
    while gameState != "Exit":
        # Reset screen
        screen.fill(bg_color)

        # User inputs
        for event in pygame.event.get():
            # Check if player close window
            if event.type == pygame.QUIT:
                gameState = "Exit"
            # Check if play restart
            if gameState == "Game Over" or gameState == "Win":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        gameState = "Exit"
                        gameInSession()
            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in grid:
                        for j in i:
                            if j.rect.collidepoint(event.pos):
                                if event.button == 1:
                                    # If player left clicked of the grid
                                    j.revealGrid()
                                    # Toggle flag off
                                    if j.flag:
                                        mineLeft += 1
                                        j.falg = False
                                    # If it's a mine
                                    if j.val == -1:
                                        gameState = "Game Over"
                                        j.mineClicked = True
                                elif event.button == 3:
                                    # If the player right clicked
                                    if not j.clicked:
                                        if j.flag:
                                            j.flag = False
                                            mineLeft += 1
                                        else:
                                            j.flag = True
                                            mineLeft -= 1

            # Check if won
        w = True
        for i in grid:
            for j in i:
                j.drawGrid()
                if j.val != -1 and not j.clicked:
                    w = False
        if w and gameState != "Exit":
            gameState = "Win"

        # Draw Texts
        if gameState != "Game Over" and gameState != "Win":
            time += 1
        elif gameState == "Game Over":
            drawText("Game Over!", 50)
            drawText("R to restart", 35, 50)
            for i in grid:
                for j in i:
                    if j.flag and j.val != -1:
                        j.mineFalse = True
        else:
            drawText("You WON!", 50)
            drawText("R to restart", 35, 50)

        # Draw time
        s = str(time // 15)
        screen_text = pygame.font.SysFont("Calibri", 50).render(s, True, (0, 0, 0))
        screen.blit(screen_text, (border, border))

        # Draw mine left
        screen_text = pygame.font.SysFont("Calibri", 50).render(mineLeft.__str__(), True, (0, 0, 0))
        screen.blit(screen_text, (screen_width - border - 50, border))

    pygame.display.update()
    timer.tick(15)  


gameInSession()
pygame.quit()
quit()
