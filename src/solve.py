import string # for ascii encoding
import board
import pieces

def tree_reccursive (pcs, id):

    brd = board.Board()       # reconstruct board
    for pc in pcs:
        brd.addpiece(pc)

    letter = string.ascii_uppercase[id]
    id += 1
    if id == 26:
        id = 0

    another = pieces.Piece_L(letter)

    if brd.fitpiece(another):
        pcs.append(another)
        pcs = tree_reccursive (pcs,  id)

    return pcs
