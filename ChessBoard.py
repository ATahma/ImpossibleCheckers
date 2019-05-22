from Player import Player

class Board():
    DIM = 8  # dimensions of a standard board
    color_map = {'white': '▓', 'black': '░'}

    def __init__(self, config=dict(), color1='white', color2='black'):
        if not config:  # if configuration is empty
            player1, player2 = [], []  # player 1 and 2 positions
            for i in range(Board.DIM):
                for j in range(Board.DIM):
                    if (i % 2 == 0) ^ (j % 2 == 1):
                        # if coord matches inital piece position
                        if i < 3:  # piece is upper
                            player1.append((i, j))
                        elif i > 4:  # piece is lower
                            player2.append((i, j))
            self.player1 = Player(player1, color1)
            self.player2 = Player(player2, color2)

    def next(self, pos, player):
        if player == 1:
            pass
        elif player == 2:
            pass
        else:
            return False
    
    def __str__(self):
        board = ''
        for i in range(Board.DIM):
            for j in range(Board.DIM):
                board += '|'
                if (i, j) in self.player1.positions:
                    board += Board.color_map[self.player1.color]
                elif (i, j) in self.player2.positions:
                    board += Board.color_map[self.player2.color]
                else:
                    board += ' '
                if j == Board.DIM - 1:
                    board += '|\n'
        return board

    def __repr__(self):
        return 'Board({}, {}, {})'.format(self.states, self.c1, self.c2)

B = Board()
print(B)
