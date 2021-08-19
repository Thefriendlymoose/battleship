import boardclass
import boatclass
import actionsclass


boat1 = boatclass.Boat(4, 1, 0, True)
boat4 = boatclass.Boat(3, 0, 0, False)

shot1 = actionsclass.Actions(1,1,"david")
shot2 = actionsclass.Actions(3,3,"david")
shot1.updateShotBoard(d, shot)
shot2.updateShotBoard(d, shot)

d.printBoard()
shot.printBoard()

#Variables

player1 = ""
player2 = ""
board1 = ""
board2 = ""
shotBoard1 = ""
shotBoard2 = ""

boatSizes = [5, 5, 4, 3, 3, 2, 2]
gridSizes = [10, 20]
gameSize = ""

#INIT

player1 = input("advise your name: ")
player2 = input("advise your name: ")

gameSize = input("please advise following game size %r: " %gridSizes)

board1 = boardclass.Board(player1, len(boatSizes), gameSize, "boats")
board2 = boardclass.Board(player2, len(boatSizes), gameSize, "boats")
shotBoard1 = boardclass.Board(player1, len(boatSizes), gameSize, "shots")
shotBoard2 = boardclass.Board(player2, len(boatSizes), gameSize, "shots")


    
