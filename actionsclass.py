class Actions:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY


#in below functions you send the otherplayers boatBoard and current player shotBoard

    def hitOrMiss(self, boatBoard, shotBoard):
        if shotBoard.returnCell(self.posX, self.posY) == "o":
            if boatBoard.returnCell(self.posX, self.posY) == "x":
                return True
            else:
                return False
            
    def updateShotBoard(self, boatBoard, shotBoard):
        if self.hitOrMiss(boatBoard, shotBoard) == True:
            shotBoard.updateBoard(self.posX, self.posY, "H")
            boatBoard.updateBoard(self.posX, self.posY, "D")
            return True
        elif shotBoard.returnCell(self.posX, self.posY) != "o":
            print("you have already shot here please shoot again")
            return False
        else:
            shotBoard.updateBoard(self.posX, self.posY, "M")
            return True
