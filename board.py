from coord import Coord

class Board:

    board = []

    def __init__(self, width = 8, height = 8):
        list.__init__([])   # is this essential boilerplate?
        self.width = width
        self.height = height
        self.board = self.emptyboard(self.width, self.height)

    # "DATABASE" / UPDATE
    def setSq (self, coord, ele):
        self.board [coord.x][coord.y] = ele

    def getSq (self, coord):
        return self.board [coord.x][coord.y]

    def addpiece (self, pc):
        self.setSq(pc.focus, pc.name)
        for coord in pc.figure:
            relative = Coord(pc.focus.x + coord.x, pc.focus.y + coord.y)
            self.setSq(relative, pc.name)

    # TEST FIT
    def fitpiece (self, pc):
        if not self.squarefree (pc.focus):
            return False
        for coord in pc.figure:
            relative = Coord(pc.focus.x + coord.x, pc.focus.y + coord.y)
            if not self.squarefree(relative):
                return False
        return True


    def squarefree (self, coord):
        if coord.x < 0 or coord.x > self.width:
            return False
        if coord.y < 0 or coord.y > self.height:
            return False
        if self.board [coord.x][coord.y]:  # has anything in it
            return False
        else:
            return True



    # "GRAPHICS" / CANVAS
    def paint (self):
        for row in self.board:
            output = ""
            for sq in row:
                if sq:
                    output = output + sq + " "
                else:
                    output += "- "
            print (output)

    # "INITIALISE" / SETUP
    def emptyboard (self, width, height):
        count = 0
        newarray = []
        while count < height:
            newarray.append(self.emptyrow (width))
            count += 1
        return newarray

    def emptyrow (self, width):
        count = 0
        newarray = []
        while count < width:
            newarray.append(None)
            count += 1
        return newarray
