import boardclass
import boatclass
import actionsclass

#####TEMP######
def checkGamesizeInput(userInput):
    try:
        temp = int(userInput)
        print("is int")
        return True
    except ValueError:
        try:
            temp = float(userInput)
            print("is float")
            return False
        except ValueError:
            print("is string")
            return False

def checkGamesizeSize(userInput):
    for elem in gridSizes:
        print(elem)
        if elem == userInput:
            return True
    return False

def returnBoatNameAndSize(boatSize):
    switcher = {
        2: "Patrol Boat: 2 Cells",
        3: "Cruiser: 3 Cells",
        4: "Battleship: 4 Cells",
        5: "Carrier: 5 Cells",

    }
    return switcher.get(boatSize)

#Variables

player1 = ""
player2 = ""
board1 = ""
board2 = ""
shotBoard1 = ""
shotBoard2 = ""

boatSizes = [5, 5, 4, 4, 3, 3, 2, 2]
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
            print("did i get here")
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

for i in range(len(boatSizes)):
    placeBoat = input("%r Input Row, Col and Rot: " % returnBoatNameAndSize(boatSizes[i]))
    userInputArray= placeBoat.split()
    boatRow = int(userInputArray[0])
    boatCol = int(userInputArray[1])
    boatRot = userInputArray[2]
    if boatRot == "V":
        boatRot = True
    else:
        boatRot = False
    
    tempBoat = boatclass.Boat(boatSizes[i], boatCol, boatRow, boatRot)

    placementPossible = True

    while placementPossible:
        if board1.checkPlacementPossible(tempBoat):
            board1.addBoat(tempBoat)
            placementPossible = False
        else:
            print("Boat Placement failed")
            placeBoat = input("%r Input Row, Col and Rot: " % returnBoatNameAndSize(boatSizes[i]))
            userInputArray= placeBoat.split()
            boatRow = int(userInputArray[0])
            boatCol = int(userInputArray[1])
            boatRot = userInputArray[2]
            if boatRot == "V":
                boatRot = True
            else:
                boatRot = False
            tempBoat = boatclass.Boat(boatSizes[i], boatCol, boatRow, boatRot) 
    board1.printBoard()
                      

board1.printBoard()

    



