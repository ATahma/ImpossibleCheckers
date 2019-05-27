from Board import Board
from Piece import Piece

'''beginnings of a machine learning implementation'''

def R(board, player, move_type, piece, destination):
    '''reward function for a specific move'''
    b = board.copy()
    if player == 1:
        p = b.player1  # active player
        o = b.player2  # opponent
    elif player == 2:
        p = b.player2  # active player
        o = b.player1  # opponent
    else:
        raise('invalid player', player)
    if move_type == 'move':
        p.move(o, piece, destination)
    elif move_type == 'capture':
        p.capture(o, piece, destination)
    else:
        raise('invalid move type', move_type)

    winner = b.winner()
    if winner == p:
        return 0.0
    elif winner == 0:
        return -100.0

    if not o.legalMoves(p) and o.legalCaptures(p):  # tie
        return -0.5
    else:
        return -1.0

b = Board()
print(R(b, 1, 'move', Piece((2, 0), 'white'), (3, 1)))
