from Player import Player

class Board():
    DIM = 8  # dimensions of a standard board

    def __init__(self, player1=set(), player2=set(), color1='white', color2='black'):
        if not player1 and not player2:  # if configuration is empty
            for i in range(Board.DIM):
                for j in range(Board.DIM):
                    if (i % 2 == 0) ^ (j % 2 == 1):
                        # if coord matches inital piece position
                        if i < 3:  # piece is upper
                            player1.add((i, j))
                        elif i > 4:  # piece is lower
                            player2.add((i, j))
        self.player1 = Player(player1, color1)
        self.player2 = Player(player2, color2)
        # store player 1 and 2 positions and color


    def __str__(self):
        '''graphical representation of checkers board'''
        color_map = {'white': '▓', 'black': '░'}
        board = ''
        for i in range(Board.DIM):
            for j in range(Board.DIM):
                board += '|'
                if (i, j) in self.player1.positions:
                    board += color_map[self.player1.pieces[(i, j)].color]
                    # get color from piece dict
                elif (i, j) in self.player2.positions:
                    board += color_map[self.player2.pieces[(i, j)].color]
                    # get color from piece dict
                else:
                    board += ' '
                if j == Board.DIM - 1:
                    board += '|\n'  # end of line
        return board

    def __repr__(self):
        '''representation of Board class'''
        p1, p2 = self.player1.pieces, self.player2.pieces
        return 'Board({}, {}, \'{}\', \'{}\')'.format(p1.keys(), p2.keys(), p1.values(), p2.values())

if __name__ == '__main__':
    B = Board()
    print(B)
    #print(B.__repr__())
    print(*[i for i in B.player1.legalMoves(B.player2, 'down')], sep='\n')
    #print(*[i for i in B.player2.legalMoves(B.player1, 'up')], sep='\n')
    print(*[i for i in B.player1.legalCaptures(B.player2, 'down')], sep='\n')
    print(*[i for i in B.player2.legalCaptures(B.player1, 'up')], sep='\n')
