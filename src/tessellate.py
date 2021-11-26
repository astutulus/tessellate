
import situation
import solve

pieceslist = []
identifier = 0

pieceslist = solve.tree_reccursive(pieceslist, identifier)

board = situation.Board()       # reconstruct board
print()
for pc in pieceslist:
    board.addpiece(pc)
    print (pc)
print()
board.paint()
