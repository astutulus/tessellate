import board
import piece

brd = board.Board()
pcs = (piece.Piece("A"), piece.Piece("B"), piece.Piece("C"))

for pc in pcs:

    if (brd.fitpiece (pc)):
        brd.addpiece (pc)
        brd.paint()
        print ("fitted", pc)
    else:
        print ("didn't fit", pc)
