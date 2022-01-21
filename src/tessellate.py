
import board
import solve

identifier = 0

pieceslist = solve.tree_reccursive(pieceslist, identifier)

board = board.Board()       # reconstruct board
print()
for pc in pieceslist:
    board.addpiece(pc)
    print (pc)
print()
board.paint()
