from coord import Coord

class Piece:

    def __init__(self, name):
        self.name = name
        self.focus = Coord(0,0)
        self.figure = (Coord(0,1), Coord(0,-1), Coord(-1,-1))

    def rotate(self):
        for coord in self.figure:
            coord.x, coord.y = coord.y, coord.x
            coord.y = coord.y * -1

    def __str__(self):
        # return "piece " + self.name + ' x: ' + str(self.focus.x) + ' y: ' + str(self.focus.y)

        return "Piece " + self.name + " position is  " + str(self.focus)
