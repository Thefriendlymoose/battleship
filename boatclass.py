#rotataion boolean: if true then boat vertical else horizontal

class Boat:
    def __init__(self, size, posX, posY, rot):
        self.size = size
        self.posX = posX
        self.posY = posY
        self.rot = rot


    def returnPosX(self):
        return self.posX

    def returnPosY(self):
        return self.posY

    def returnSize(self):
        return self.size

    def returnRot(self):
        return self.rot
