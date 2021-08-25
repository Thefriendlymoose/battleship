import boardclass
import boatclass
import actionsclass
import os
import time

#####TEMP######
def checkGamesizeInput(userInput):
    try:
        temp = int(userInput)
        return True
    except ValueError:
        try:
            temp = float(userInput)
            return False
        except ValueError:
            return False

def checkGamesizeSize(userInput):
    for elem in gridSizes:
        if elem == userInput:
            return True
    return False

def returnBoatNameAndSize(boatSize):
    switcher = {
        2: "Patrol Boat, 2 Cells long",
        3: "Cruiser, 3 Cells long",
        4: "Battleship, 4 Cells long",
        5: "Carrier, 5 Cells long",
    }
    return switcher.get(boatSize)

def cls():
    print ("\n" * 100)

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\n")
        time.sleep(1)
        t -= 1

# now, to clear the screen



#Variables

player1 = ""
player2 = ""
board1 = ""
board2 = ""
shotBoard1 = ""
shotBoard2 = ""
#4, 4, 3, 3, 2, 2
boatSizes = [2]
gridSizes = [10, 20]
gameSize = ""

#INIT

player1 = input("advise your name: ")
player2 = input("advise your name: ")
gameSize = input("please advise following game size %r: " %gridSizes)

#Checks if gameSize input is correct
inputCorrect = True
while inputCorrect:
    if checkGamesizeInput(gameSize):
        gameSize = int(gameSize)
        if checkGamesizeSize(gameSize):
            inputCorrect = False
        else:
           gameSize = input("wrong input: please advise following game size %r: " %gridSizes)
    else:
        gameSize = input("wrong input: please advise following game size %r: " %gridSizes)




board1 = boardclass.Board(player1, len(boatSizes), gameSize, "boats")
board2 = boardclass.Board(player2, len(boatSizes), gameSize, "boats")
shotBoard1 = boardclass.Board(player1, len(boatSizes), gameSize, "shots")
shotBoard2 = boardclass.Board(player2, len(boatSizes), gameSize, "shots")

board1.createBoard()
board2.createBoard()
shotBoard1.createBoard()
shotBoard2.createBoard()

boatBoards = [board1, board2]
shotBoards = [shotBoard1, shotBoard2]

#user input must be in format 1 1 V


for elem in boatBoards:
    for i in range(len(boatSizes)):
##      place input checking mechanism here
##      we need to check wether the DATA in placeBoat is in format "1 1 V"
        elem.printBoard()
        boatRow = input("Player: {} \nBoat: {} \nPlease enter row 0-9: ".format(elem.returnPlayer(),returnBoatNameAndSize(boatSizes[i])))
        row = True
        while row:
            if checkGamesizeInput(boatRow):
                boatRow = int(boatRow)
                if boatRow < gameSize and boatRow >= 0:
                    row = False
                else:
                    boatRow = input("numbers between 0 and {}".format(gameSize-1))
            else:
                boatRow = input("only numbers Row")

        boatCol = input("Player: {} \nBoat: {} \nPlease enter column 0-9: ".format(elem.returnPlayer(),returnBoatNameAndSize(boatSizes[i])))
        col = True
        while col:
            if checkGamesizeInput(boatCol):
                boatCol = int(boatCol)
                if boatCol<gameSize and boatCol >= 0:
                    col = False
                else:
                    boatCol = input("numbers between 0 and {}".format(gameSize-1))
            else:
                boatCol = input("only numbers Col")

        boatRot = input("Player: {} \nBoat: {} \nPlease enter rotation H for Horizontal or V for Vertical: ".format(elem.returnPlayer(),returnBoatNameAndSize(boatSizes[i])))
        rot = True
        while rot:
            if boatRot == "V" or boatRot == "H":
                rot = False
            else:
                boatRot = input("please give correct input")


        if boatRot == "V":
            boatRot = True
        else:
            boatRot = False
        
        tempBoat = boatclass.Boat(boatSizes[i], boatCol, boatRow, boatRot)

        placementPossible = True

        while placementPossible:
            if elem.checkPlacementPossible(tempBoat):
                elem.addBoat(tempBoat)
                placementPossible = False
            else:
                print("Boat Placement failed")

                boatRow = input("row here")
                row = True
                while row:
                    if checkGamesizeInput(boatRow):
                        boatRow = int(boatRow)
                        if boatRow < gameSize and boatRow >= 0:
                            row = False
                        else:
                            boatRow = input("numbers between 0 and {}".format(gameSize-1))
                    else:
                        boatRow = input("only numbers Row")

                boatCol = input("col here")
                col = True
                while col:
                    if checkGamesizeInput(boatCol):
                        boatCol = int(boatCol)
                        if boatCol<gameSize and boatCol >= 0:
                            col = False
                        else:
                            boatCol = input("numbers between 0 and {}".format(gameSize-1))
                    else:
                        boatCol = input("only numbers Col")

                boatRot = input("rot here")
                rot = True
                while rot:
                    if boatRot == "V" or boatRot == "H":
                        rot = False
                    else:
                        boatRot = input("please give correct input")
                if boatRot == "V":
                    boatRot = True
                else:
                    boatRot = False
                tempBoat = boatclass.Boat(boatSizes[i], boatCol, boatRow, boatRot)

    elem.printBoard()
    countdown(3)
    cls()
    countdown(3)
                          
gameOver = True

while gameOver:
    for i in range(len(boatBoards)):
##      place input checking mechanism here
##      we need to check wether the data in shot is in format "1 1"
        shotBoards[i].printBoard()
        shotRow = input("row here")
        row = True
        while row:
            if checkGamesizeInput(shotRow):
                shotRow = int(shotRow)
                if shotRow < gameSize:
                   row = False
                else:
                    shotRow = input("numbers between 0 and {}".format(gameSize-1))
            else:
                shotRow = input("Please input a number between 0 and {}".format(gameSize-1))


        shotCol = input("Input column here: ")
        col = True
        while col:
            if checkGamesizeInput(shotCol):
                shotCol = int(shotCol)
                if shotCol < gameSize:
                   col = False
                else:
                    shotCol = input("numbers between 0 and {}".format(gameSize-1))
            else:
                shotCol = ("Please input a number between 0 and {}".format(gameSize-1))       

        tempShot = actionsclass.Actions(shotCol, shotRow)
        
        if i == 0:
            tempShot.updateShotBoard(boatBoards[i+1], shotBoards[i])
        else:
            tempShot.updateShotBoard(boatBoards[i-1], shotBoards[i])

        if i == 0:
            if boatBoards[i+1].checkIfLost():
                print("{} wins the game!".format(boatBoards[i].returnPlayer()))
                gameOver = False
                break
        else:
            if boatBoards[i-1].checkIfLost():
                print("{} wins the game!".format(boatBoards[i].returnPlayer()))
                gameOver = False
                break

        boatBoards[i].printBoard()
        shotBoards[i].printBoard()
        countdown(3)
        cls()
        countdown(3)
