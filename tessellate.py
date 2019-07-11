import board
import piece

brd = board.Board()
pca = piece.Piece("A")

if (brd.fitpiece (pca)):
    brd.addpiece (pca)
    brd.paint()
    print ("fitted")
else:
    print ("didn't fit at" , pca.focus.toString())
