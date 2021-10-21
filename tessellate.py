import string # for ascii encoding
import board
import piece

def reccursive (pcs, id):

    brd = board.Board()       # reconstruct board
    for pc in pcs:
        brd.addpiece(pc)

    letter = string.ascii_uppercase[id]
    id += 1
    if id == 26:
        id = 0

    another = piece.Piece (letter)

    if brd.fitpiece(another):
        pcs.append(another)
        pcs = reccursive (pcs,  id)

    return pcs

# test comment

pieceslist = []
identifier = 0

pieceslist = reccursive(pieceslist, identifier)

board = board.Board()       # reconstruct board
print()
for piece in pieceslist:
    board.addpiece(piece)
    print (piece)
print()
board.paint()
