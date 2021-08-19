import boardclass
import boatclass
import actionsclass

d = boardclass.Board("david", 5, 10, "boats")
shot = boardclass.Board("david", 5, 10, "shots")
d.createBoard()
shot.createBoard()




boat1 = boatclass.Boat(4, 1, 0, True)
boat4 = boatclass.Boat(3, 0, 0, False)

d.addBoat(boat1)
d.printBoard()
d.addBoat(boat4)

d.printBoard()

shot1 = actionsclass.Actions(1,1,"david")
shot2 = actionsclass.Actions(3,3,"david")
shot1.updateShotBoard(d, shot)
shot2.updateShotBoard(d, shot)

d.printBoard()
shot.printBoard()
