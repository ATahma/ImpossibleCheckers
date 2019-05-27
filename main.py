'''
Matteo Gisondi, 1730913, Samuel Park, 1732027, Ali Tahmasebi, 1730131
Friday, May 24
R. Vincent, instructor
Final Project
'''

def main():
    '''a "game" (just a combination of up to 150 arbitrary moves)'''
    from Board import Board
    B = Board()  # initialize board
    print(B)
    from random import choice
    from time import sleep
    p1, p2 = B.player1, B.player2  # get players
    while True:  #  if a capture is possible, capture, else move
        mPiece = input('Please enter two integers, separated by a comma, to represent the coordinates of the piece you wish to move.')
        mPos = input('Please enter two integers, separated by a comma, to represent the coordinates of the location you wish to move to.')
        mPiece = mPiece.split(',')
        mPos = mPos.split(',')  
        try:
            mPiece = tuple(map(int, mPiece))
            print(mPiece)
            mPos = tuple(map(int, mPos))
            print(mPos)
            mPiece = B.player1.pieces[mPiece]
        except:
            print('You did not choose valid integers.')
            continue
        if (mPiece, mPos) in B.player1.legalMoves(B.player2):
            B.player1.move(B.player2, mPiece, mPos)
        elif (mPiece, mPos) in p1.legalCaptures(p2):
            B.player1.capture(p2, mPiece, mPos)
        else:
            print('Move is not valid.')
            continue

        print(B)

        winner = B.winner()
        if winner:  # check for winner
            print('{} won.'.format(winner.color().title()))
            break

        try:
            capture_p2 = choice([i for i in p2.legalCaptures(p1)])
            capture = p2.capture(p1, capture_p2[0], capture_p2[1])
            print('Capture {}\n'.format(capture))
        except:
            try:
                move_p2 = choice([i for i in p2.legalMoves(p1)])
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

if __name__ == '__main__':
    main()
