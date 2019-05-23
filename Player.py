from Piece import Piece

class Player():
    '''keep track of piece positions and color of pieces'''
    DIM = 8

    def __init__(self, positions, color):
        self.positions = positions  # set of piece positions
        self.pieces = {i:Piece(i, color) for i in self.positions}
        # dict of piece objects associated to position

    def legalMoves(self, other, direction):
        '''set of all legal moves'''
        legal_moves = set()
        for i, j in self.positions:
            if self.pieces[(i, j)].state == 2:  # piece is promoted
                rows = (i - 1, i + 1)  # check above and below
            elif direction == 'down':
                rows = (i + 1,)  # check below
            elif direction == 'up':
                rows = (i - 1,)  # check above
            else:
                raise('No direction specified')
            l_col, r_col = j - 1, j + 1
            for next_row in rows:  # check up, down, or both
                for next_col in (l_col, r_col):  # check left and right
                    try:
                        assert 0 <= next_row < Player.DIM
                        assert 0 <= next_col < Player.DIM  # move square exists
                        assert (next_row, next_col) not in self.positions
                        assert (next_row, next_col) not in other.positions
                        # destination space is not occupied
                        legal_moves.add((self.pieces[(i, j)], (next_row, next_col)))
                    except:
                        pass
        return legal_moves

    def legalCaptures(self, other, direction):  # revise
        '''set of all legal captures'''
        legal_captures = set()
        for i, j in self.positions:
            if self.pieces[(i, j)].state == 2:  # piece is promoted
                rows, rows2 = (i - 1, i - 2), (i + 1, i + 2)  # check above and below
            elif direction == 'down':
                rows, rows2 = (i + 1, -1), (i + 2, -1)  # check below (-1 is filler)
            elif direction == 'up':
                rows, rows2 = (i - 1, -1), (i + 2, -1)  # check above (-1 is filler)
            else:
                raise('No direction specified: down = player1, up = player2')
            l_col, l_col2, r_col, r_col2 = j - 1, j - 2, j + 1, j + 2
            for next_row, next_row2 in rows, rows2:
                for next_col in (l_col, r_col):
                    for next_col2 in (l_col2, r_col2):  # check left and right
                        try:
                            assert 0 <= next_row2 < Player.DIM
                            assert 0 <= next_col2 < Player.DIM  # move square exists
                            assert (next_row, next_col) not in self.positions
                            assert (next_row, next_col) in other.positions
                            assert (next_row2, next_col2) not in self.positions
                            assert (next_row2, next_col2) not in other.positions
                            # intermediate space is occupied by enemy piece, not by friendly
                            # destination space is not occupied
                            legal_captures.add((self.pieces[(i, j)], (next_row2, next_col2)))
                        except:
                            pass
        return legal_captures

    def isLegalMove(self, other, piece, destination):  # drastically inefficient
        '''check if a move is legal'''
        if destination[0] < piece.pos[0]:
            direction = 'up'
        elif destination[0] > piece.pos[0]:
            direction = 'down'
        else:
            return False
        if (piece, destination) in self.legalMoves(other, direction):
            return True
        return False

    def isLegalCapture(self, other, piece, destination):  # drastically inefficient
        '''check if a capture is legal'''
        if destination[0] < piece.pos[0]:
            direction = 'up'
        elif destination[0] > piece.pos[0]:
            direction = 'down'
        else:
            return False
        if (piece, destination) in self.legalMoves(other, direction):
            return True
        return False

    def move(self, other, piece, destination):
        if self.isLegalMove(other, piece, destination):
            self.positions.remove(piece.pos)
            del_piece = self.pieces.pop(piece.pos)
            color = del_piece.color
            self.pieces[destination] = Piece(destination, color)
            self.positions.add(destination)
        else:
            return False

    def removePiece(self, piece):
        self.positions.remove(piece.pos)
        self.pieces.pop(piece.pos)

    def capture(self, other, piece, destination):
        if self.isLegalCapture(other, piece, destination):
            self.positions.remove(piece.pos)
            inter_x = piece.pos[0] + destination[0] // 2
            inter_y = piece.pos[1] + destination[1] // 2
            other.removePiece(other.pieces[(inter_x, inter_y)])
            del_piece = self.pieces.pop(piece.pos)
            color = del_piece.color
            self.pieces[destination] = Piece(destination, color)
            self.positions.add(destination)

    def promote(self, piece):
        self.pieces[piece.pos].state = 2

    def __repr__(self):
        return 'Player({}, {})'.format(self.positions, self.color)
