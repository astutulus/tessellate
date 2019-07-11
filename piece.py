from coord import Coord

class Piece:
    name = ""
    focus = Coord(4,4)
    figure = (Coord(0,1), Coord(0,-1), Coord(-1,-1))

    def __init__(self, name):
        list.__init__([])
        self.name = name
