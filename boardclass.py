#Battleship
#Test

class Board:
    def __init__(self, player, boats, gridSize, boardType):
        self.player = player
        self.boats = boats
        self.gridSize = gridSize
        self.board = []
        self.boardType = boardType
        
    def printBoard(self):
        for elem in self.board:
            print(" ".join(elem))

        print("-----------------------------")

    def createBoard(self):
        for x in range(0, self.gridSize):
            self.board.append(["o"] * self.gridSize)

    def updateBoard(self, posX, posY, cat):
        self.board[posY][posX] = cat

    def returnCell(self, posX, posY):
        return self.board[posY][posX]

    def returnGridSize(self):
        return self.gridSize

    def addBoat(self, boat):
        if self.checkBounds(boat) == True and self.checkBoatExist(boat) == True:
            if boat.returnRot() == True:
                for i in range(boat.returnSize()):
                    self.updateBoard(boat.returnPosX(),boat.returnPosY() + i, "x")
            else:
                for i in range(boat.returnSize()):
                    self.updateBoard(boat.returnPosX() + i,boat.returnPosY(), "x")
        else:
            print("place again")
            
    def checkBounds(self, boat):
        if boat.returnRot() == False:
            if((self.returnGridSize() - 1 - boat.returnPosX()) < boat.returnSize()):
                print("horizontal out of bounds")
                return False
            else:
                print("horizontal can be placed")
                return True
        else:
            if((self.returnGridSize() - 1 - boat.returnPosY()) < boat.returnSize()):
                print("vertical out of bounds")
                return False
            else:
                print("vertical can be place")
                return True

    def checkBoatExist(self, boat):
        for i in range(boat.returnSize()):
            if boat.returnRot() == True:
                print("vertical")
                if "x" in self.returnCell(boat.returnPosX(), (boat.returnPosY() + i)):
                    print("boat exist")
                    return False
            else:
                print("horizontal")
                if "x" in self.returnCell((boat.returnPosX() + i), boat.returnPosY()):
                    print("boat exist")
                    return False
        return True
                
