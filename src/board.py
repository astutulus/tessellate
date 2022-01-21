from coord import Coord

class Board:

    size = 4


    def __init__(self):

        self.width = self.size
        self.height = self.size
        self.board = self.emptyboard(self.width, self.height)
        self.pieceslist = []


    # "INITIALISE" / SETUP
    def emptyboard (self, width, height):
        return [([None] * width) for h in range(height)]

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
        fitted = False
        for x in range(self.width - 1):         # LOOP 1

            for y in range (self.height - 1):   # LOOP 2

                pc.focus.x = x
                pc.focus.y = y
                print ('x', x , ', ' , 'y', y)
                for angle in [0, 90, 180, 270]: # LOOP 3
                    if self.isfitting (pc, angle):
                        fitted = True
                        break           # FROM LOOP 3
                    print ('Rotating' , pc.name , 'to' , angle)
                    pc.rotate()

                if fitted:
                    break               # FROM LOOP 2

            if fitted:
                break                   # FROM LOOP 1
        # RETURN A VALUE:
        return fitted

    def isfitting (self, pc, angle):
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
