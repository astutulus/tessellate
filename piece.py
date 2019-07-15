from coord import Coord

class Piece:
    name = ""
    focus = Coord(4,4)
    figure = (Coord(0,1), Coord(0,-1), Coord(-1,-1))

    def __init__(self, name):
        list.__init__([])
        self.name = name

    def rotate(self):
        for coord in self.figure:

            coord.x, coord.y = coord.y, coord.x
            coord.y = coord.y * -1

    def __str__(self):
        return "piece " + self.name
