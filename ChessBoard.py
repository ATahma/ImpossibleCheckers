from Piece import Piece

class Board():
    DIM = 8
    color_map = {'white': '░', 'black': '▓'}
    def __init__(self, config=dict(), c1='cyan', c2='blue'):
        self.c1, self.c2 = c1, c2
        self.p1, self.p2 = 12, 12
        self.states = config
        if not config:  # if configuration is empty
            for i in range(Board.DIM):
                for j in range(Board.DIM):
                    if ((i % 2) == 0) ^ ((j % 2) == 1):
                        if i < 3:
                            self.states[Piece((i, j))] = color_map[c1]
                        elif i > 4:
                            self.states[Piece((i, j))] = color_map[c2]

    def next(self, pos, player):
        if player == 1:
            pass
        elif player == 2:
            pass
        else:
            return False
    
    def __str__(self):
        line = '_' * 41 + '\n'
        board = line
        for i in range(Board.DIM):
            for j in range(Board.DIM):
                board += '|'
                if (i, j) in [p.pos for p in self.states.keys()]:
                    board += self.states[p] + '|'
                else:
                    board += ' '
            board += line + '\n'
        return board

    def __repr__(self):
        return 'Board({}, {}, {})'.format(self.states, self.c1, self.c2)

B = Board()
print(B)
