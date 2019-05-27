'''
Matteo Gisondi, 1730913, Samuel Park, 1732027, Ali Tahmasebi, 1730131
Friday, May 24
R. Vincent, instructor
Final Project
'''

from Piece import Piece
import numpy as np

class Player():
    '''keep track of piece positions and color of pieces'''
    DIM = 8  # dimensions of a standard board

    def __init__(self, positions, color, direction):
        self.positions = positions  # set of piece positions
        self.pieces = {i:Piece(i, color) for i in self.positions}
        # dict of piece objects associated to position
        self.direction = direction  # direction of moves
        self.crowned() # update crowned pieces
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
    def crowned(self):
        """
        Added by Ali
        return an array of uncrowned and crowned pieces
        as tuple in repsective orded
        """
        # numpy arrays fro crowned and uncrowned
        self.crowned = []
        self.uncrowned = []
        for piece in self.pieces.values(): # iterate over all the pieces
            # check state
            if piece.state == 2:
                # append to proper array
                self.crowned.append(piece)
            else:
                self.uncrowned.append(piece)
        # numpy acts weird when you try to append a user defined object to an array
        # so i turn the lists into arrays at the end
        self.crowned, self.uncrowned = np.array(self.crowned), np.array(self.uncrowned)
        return (self.crowned.copy(), self.uncrowned.copy())

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

    def move(self, other, piece, destination):
        '''update self and other positions for piece move
        must make move based on list of legal moves'''
        self.positions.remove(piece.pos)  # remove current position
        del_piece = self.pieces.pop(piece.pos)  # remove current piece
        self.pieces[destination] = Piece(destination, del_piece.color, del_piece.state)
        self.positions.add(destination)
        self.promote(self.pieces[destination])
        # add new piece and check for promotion
        self.crowned() # update the crowned pieces          
        return (piece, destination)

    def removePiece(self, piece):
        self.positions.remove(piece.pos)
        self.pieces.pop(piece.pos)
        self.crowned() # update the crowned pieces    

    def capture(self, other, piece, destination):
        '''update self and other positions for piece capture
        must capture based on list of legal captures'''
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
        self.crowned() # update the crowned pieces      
        return (piece, destination)

    def promote(self, piece):
        if self.direction == 'down':
            limit = 7
        elif self.direction == 'up':
            limit = 0
        if piece.pos[0] == limit:
            self.pieces[piece.pos].state = 2
        self.crowned() # update the crowned pieces    
    def __repr__(self):
        return 'Player({}, {})'.format(self.positions, self.color(), self.direction)
