'''
Matteo Gisondi, 1730913, Samuel Park, 1732027, Ali Tahmasebi, 1730131
Friday, May 24
R. Vincent, instructor
Final Project
'''

from Piece import Piece

class Player():
    '''keep track of piece positions and color of pieces'''
    DIM = 8  # dimensions of a standard board

    def __init__(self, positions, color, direction):
        self.positions = positions  # set of piece positions
        self.pieces = {i:Piece(i, color) for i in self.positions}
        # dict of piece objects associated to position
        self.direction = direction  # direction of moves
    
    def color(self):
        return self.pieces[list(self.positions)[0]].color

    def legalMoves(self, other):
        '''set of all legal moves'''
        legal_moves = set()
        for i, j in self.positions:
            if self.pieces[(i, j)].state == 2:  # piece is promoted
                rows = (i - 1, i + 1)  # check above and below
            elif self.direction == 'down':
                rows = (i + 1,)  # check below
            elif self.direction == 'up':
                rows = (i - 1,)  # check above
            else:
                raise('No direction specified')
            for next_row in rows:  # check up, down, or both
                for next_col in (j - 1, j + 1):  # check left and right
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

    def legalCaptures(self, other):
        '''set of all legal captures'''
        legal_captures = set()
        for i, j in self.positions:
            if self.pieces[(i, j)].state == 2:  # piece is promoted
                rows = ((i - 1, i - 2), (i + 1, i + 2))  # check above and below
            elif self.direction == 'down':
                rows = ((i + 1, i + 2),)  # check below
            elif self.direction == 'up':
                rows = ((i - 1, i - 2),)  # check above
            else:
                raise('No direction specified: down = player1, up = player2')
            for next_row, next_row2 in rows:
                for next_col, next_col2 in ((j - 1, j - 2), (j + 1, j + 2)):
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
        if (piece, destination) in self.legalMoves(other):
            return True
        return False

    def isLegalCapture(self, other, piece, destination):  # drastically inefficient
        '''check if a capture is legal'''
        if (piece, destination) in self.legalCaptures(other):
            return True
        return False

    def move(self, other, piece, destination):
        if self.isLegalMove(other, piece, destination):
            self.positions.remove(piece.pos)  # remove current position
            del_piece = self.pieces.pop(piece.pos)  # remove current piece
            self.pieces[destination] = Piece(destination, del_piece.color, del_piece.state)
            self.positions.add(destination)
            self.promote(self.pieces[destination])
            # add new piece and check for promotion
            return (piece, destination)
        else:
            return False

    def removePiece(self, piece):
        self.positions.remove(piece.pos)
        self.pieces.pop(piece.pos)

    def capture(self, other, piece, destination):
        '''update self and other positions for piece capture'''
        if self.isLegalCapture(other, piece, destination):
            self.positions.remove(piece.pos)  # remove current position
            inter_x = (piece.pos[0] + destination[0]) // 2
            inter_y = (piece.pos[1] + destination[1]) // 2
            other.removePiece(other.pieces[(inter_x, inter_y)])
            # remove intermediate piece
            del_piece = self.pieces.pop(piece.pos)  # remove current piece
            self.pieces[destination] = Piece(destination, del_piece.color, del_piece.state)
            self.positions.add(destination)
            self.promote(self.pieces[destination])
            # add new piece and check for promotion
            return (piece, destination)
        else:
            return False

    def promote(self, piece):
        if self.direction == 'down':
            limit = 7
        elif self.direction == 'up':
            limit = 0
        if piece.pos[0] == limit:
            self.pieces[piece.pos].state = 2

    def __repr__(self):
        return 'Player({}, {})'.format(self.positions, self.color(), self.direction)
