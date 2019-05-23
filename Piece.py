class Piece():
    def __init__(self, pos, color, state=1):
        self.pos = pos
        self.color = color
        self.state = state

    def __repr__(self):
        if self.state == 1:
            return 'Piece({}, {})'.format(self.pos, self.color)
        return 'Piece({}, {}, {})'.format(self.pos, self.color, self.state)
