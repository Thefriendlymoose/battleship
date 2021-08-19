class Actions:
    def __init__(self, posX, posY, player):
        self.posX = posX
        self.posY = posY
        self.player = player

    def hitOrMiss(self, board):
        if board.returnCell(self.posX, self.posY) == "x":
            return True
        else:
            return False
            
    def updateShotBoard(self, boatBoard, shotBoard):
        if self.hitOrMiss(boatBoard) == True:
            shotBoard.updateBoard(self.posX, self.posY, "H")
        else:
            shotBoard.updateBoard(self.posX, self.posY, "M")
        
        
