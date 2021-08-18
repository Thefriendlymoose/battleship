#Battleship
#Test

class Board:
    def __init__(self, player, boats, gridSize):
        self.player = player
        self.boats = boats
        self.gridSize = gridSize
        self.board = []
        
    def printBoard(self):
        for elem in self.board:
            print(elem)

    def createBoard(self):
        for x in range(0, self.gridSize):
            self.board.append([0] * self.gridSize)

    def updateBoard(self, posX, posY):
        self.board[posY][posX] = "x"
        
    def addBoat(self, boat)


d = Board("david", 5, 10)
d.createBoard()
d.updateBoard(1,1)
d.printBoard()

    

