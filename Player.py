from Piece import Piece

class Player():
    '''keep track of piece positions and color of pieces'''
    def __init__(self, positions, color):
        self.color = color
        self.positions = positions
        self.pieces = (Piece(i, self.color) for i in self.positions)
    
    def legalMoves(self):
        pass
    
    def move(self, piece, destination):
        pass
    
    def removePiece(self, piece):
        pass

    def promote(self, piece):
        pass
    
    def __repr__(self):
        return 'Player({}, {})'.format(set(self.pieces), self.color)