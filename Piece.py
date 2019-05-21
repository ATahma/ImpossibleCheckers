class Piece():
    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
    
    def __str__(self):
        return str(self.color)

    def __repr__(self):
        return 'Piece({}, {})'.format(self.pos, self.color)
