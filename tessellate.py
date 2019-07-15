import board
import piece

brd = board.Board()

pcs = []

for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    pcs.append(piece.Piece(label))


for pc in pcs: # enumerate(pcs):
    if (brd.fitpiece (pc)):
        brd.addpiece (pc)
        print ("fitted", pc)
    else:
        print ("didn't fit", pc)

print ("result:")
brd.paint()
