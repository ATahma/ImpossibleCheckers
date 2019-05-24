'''
Matteo Gisondi, 1730913, Samuel Park, 1732027, Ali Tahmasebi, 1730131
Friday, May 24
R. Vincent, instructor
Final Project
'''

from Player import Player

class Board():
    DIM = 8  # dimensions of a standard board

    def __init__(self, player1=set(), player2=set(), color1='white', color2='black'):
        if not player1 and not player2:  # if no configuration provided
            for i in range(Board.DIM):
                for j in range(Board.DIM):
                    if (i % 2 == 0) ^ (j % 2 == 1):
                        # if coord matches initial piece position
                        if i < 3:  # piece is upper
                            player1.add((i, j))
                        elif i > 4:  # piece is lower
                            player2.add((i, j))
        self.player1 = Player(player1, color1, 'down')
        self.player2 = Player(player2, color2, 'up')
        # store player 1 and 2 positions and color with Player object

    def __str__(self):
        '''graphical representation of checkers board'''
        color_map = {'white': '▓', 'black': '░'}
        board = '    0 1 2 3 4 5 6 7\n\n'
        for i in range(Board.DIM):
            board += '{}  '.format(i)
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

    def winner(self):
        '''check for a winner'''
        if not self.player1.positions:
            return self.player2
        elif not self.player2.positions:
            return self.player1

    def __repr__(self):
        '''representation of Board class'''
        p1, p2 = self.player1.pieces, self.player2.pieces
        return 'Board({}, {}, \'{}\', \'{}\')'.format(p1.keys(), p2.keys(), p1.values(), p2.values())

if __name__ == '__main__':
    '''a "game" (just a combination of up to 150 arbitrary moves)'''
    B = Board()  # initialize board
    print(B)
    from random import choice
    p1, p2 = B.player1, B.player2  # get players
    for i in range(150):  #  if a capture is possible, capture, else move
        print('Turn', i + 1)
        captures_p1 = [i for i in p1.legalCaptures(p2)]
        if captures_p1:
            capture_p1 = choice(captures_p1)
            capture = p1.capture(p2, capture_p1[0], capture_p1[1])
            print('Capture {}\n'.format(capture))
        else:
            move_p1 = choice([i for i in p1.legalMoves(p2)])
            move = p1.move(p2, move_p1[0], move_p1[1])
            print('Move {}\n'.format(move))
        print(B)

        won = B.winner()
        if won:  # check for winner
            print('Player {} won'.format(won))
            break

        captures_p2 = [i for i in p2.legalCaptures(p1)]
        if captures_p2:
            capture_p2 = choice(captures_p2)
            capture = p2.capture(p1, capture_p2[0], capture_p2[1])
            print('Capture {}\n'.format(capture))
        else:
            move_p2 = choice([i for i in p2.legalMoves(p1)])
            move = p2.move(p1, move_p2[0], move_p2[1])
            print('Move {}\n'.format(move))
        print(B)

        won = B.winner()
        if won:  # check for winner
            print('Player {} won'.format(won))
            break
