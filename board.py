class Board:

    board = []

    def __init__(self, width = 8, height = 8):
        list.__init__([])   # is this essential boilerplate?
        self.board = self.emptyboard(width, height)

    # "DATABASE" / UPDATE
    def setSq (self, x, y, ele):
        self.board [x][y] = ele

    def getSq (self, x, y):
        return self.board [x, y]

    def addpiece (self, piece):
        self.setSq(piece.x, piece.y, piece.name)
        for sq in piece.shape:
            self.setSq(piece.x + sq[0], piece.y + sq[1], piece.name)

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
