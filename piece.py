class Piece:

    name = ""
    x = 2
    y = 2
    shape = ((0,1),(0,-1),(-1,-1))

    def __init__(self, name):
        list.__init__([])
        self.name = name

    def doesfit (board):
        # if cent is free
        if not board[self.x][self.y]:
            print ("FITS")
