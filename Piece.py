'''
Matteo Gisondi, 1730913, Samuel Park, 1732027, Ali Tahmasebi, 1730131
Friday, May 24
R. Vincent, instructor
Final Project
'''

class Piece():
    def __init__(self, pos, color, state=1):
        self.pos = pos
        self.color = color
        self.state = state
        # state = 1 regular piece, state = 2, promoted piece

    def __repr__(self):
        if self.state == 1:
            return 'Piece({}, {})'.format(self.pos, self.color)
        return 'Piece({}, {}, {})'.format(self.pos, self.color, self.state)
