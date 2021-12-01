from coord import Coord

class Piece:
    def __init__(self, name):
        self.name = name
        self.focus = Coord(0,0)

    def rotate(self):
        for coord in self.figure:
            coord.x, coord.y = coord.y, coord.x
            coord.y = coord.y * -1

    def __str__(self):
        return "Piece " + self.name + \
        " position is " + str(self.focus)



class Piece_L(Piece):
    def __init__(self, name):
        super().__init__(name)
        self.figure = (Coord(0,1), Coord(0,2), Coord(1,0))
    def__str__(self):
        return "L shape"


class Piece_I(Piece):
    def __init__(self, name):
        super().__init__(name)
        self.figure = (Coord(0,1), Coord(0,2), Coord(0,3))


class Piece_SQ(Piece):
    def __init__(self, name):
        super().__init__(name)
        self.figure = (Coord(0,1), Coord(1,0), Coord(1,1))
