'''
Matteo Gisondi, 1730913, Samuel Park, 1732027, Ali Tahmasebi, 1730131
Friday, May 24
R. Vincent, instructor
Final Project
'''

'''a "game" (just a combination of arbitrary moves)'''
from Board import Board
B = Board()  # initialize board
print(B)
from random import choice
p1, p2 = B.player1, B.player2  # get players
while True:  #  if a capture is possible, capture, else move
    try:
        capture_p1 = choice(list(p1.legalCaptures(p2)))
        capture = p1.capture(p2, capture_p1[0], capture_p1[1])
        print('Capture {}\n'.format(capture))
    except:
        try:
            move_p1 = choice(list(p1.legalMoves(p2)))
            move = p1.move(p2, move_p1[0], move_p1[1])
            print('Move {}\n'.format(move))
        except:
            print('Unable to complete a move, match is tied.')
            break
    print(B)

    winner = B.winner()
    if winner:  # check for winner
        print('{} won.'.format(winner.color().title()))
        break

    try:
        capture_p2 = choice(list(p2.legalCaptures(p1)))
        capture = p2.capture(p1, capture_p2[0], capture_p2[1])
        print('Capture {}\n'.format(capture))
    except:
        try:
            move_p2 = choice(list(p2.legalMoves(p1)))
            move = p2.move(p1, move_p2[0], move_p2[1])
            print('Move {}\n'.format(move))
        except:
            print('Unable to complete a move, match is tied.')
            break
    print(B)

    winner = B.winner()
    if winner:  # check for winner
        print('{} won.'.format(winner.color().title()))
        break
