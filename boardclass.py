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
        print("------%r------" %self.player)
        print("------%r------" %self.boardType)
        for elem in self.board:
            print(" ".join(elem))

        print("-------------------")

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
        if boat.returnRot() == True:
            for i in range(boat.returnSize()):
                self.updateBoard(boat.returnPosX(),boat.returnPosY() + i, "x")
        else:
            for i in range(boat.returnSize()):
                self.updateBoard(boat.returnPosX() + i,boat.returnPosY(), "x")
            
    def checkBounds(self, boat):
        if boat.returnRot() == False:
            if((self.returnGridSize() - boat.returnPosX()) < boat.returnSize()):
                print("horizontal out of bounds")
                return False
            else:
                return True
        else:
            if((self.returnGridSize() - boat.returnPosY()) < boat.returnSize()):
                print("vertical out of bounds")
                return False
            else:
                return True

    def checkBoatExist(self, boat):
        for i in range(boat.returnSize()):
            if boat.returnRot() == True:
                if "x" in self.returnCell(boat.returnPosX(), (boat.returnPosY() + i)):
                    print("boat exist")
                    return False
            else:
                if "x" in self.returnCell((boat.returnPosX() + i), boat.returnPosY()):
                    print("boat exist")
                    return False
        return True

    def returnBoardType(self):
        return self.boardType
                

    def checkPlacementPossible(self, boat):
        if self.checkBounds(boat) == True and self.checkBoatExist(boat) == True:
            return True
        else:
            return False
    
    def checkIfLost(self):
        for elem in self.board:
            if "x" in elem:
                return False
        return True

    def returnPlayer(self):
        return self.player


