import numpy as np
from Board import Board

class agent:
    """
    Learning class used to implement the components for reinforcement learning
    """
    # set the reward for each state
    rwin = 0.0 # win reward
    rloss = -1000.0
    rtie = -50.0 # tie reward
    rside = -1.0 # reward for each piece on the side of the board
    rmiddle = -2.0 # reward for each piece in the middles
    def __init__(self, expRate = 0, discount = 1):
        """
        Initialize a Board object with the follwoing properties
        states : all the past boards and the actions that led to them
        expRate : between 0 and 1, probability of taking a random move
        dc : the discount factor used to dampen the agent's rewards
        current : the current state
        creward : the reward for the current state
        """
        self.board = Board()
        # create a dictionary to keep track of all the past steps
        self.states = {}
        self.expRate = expRate
        self.dc = discount
        self.current = self.board.copy()
    def domain(self, verbose = False, showBoard = True):
        """
        return a tuple of lists, consisting of the possible moves for
        respectively player 1 and player 2
        also print the possible moves for display if 
        specified verbose = True (False by default)
        print the board (unless specified otherwise)
        """
        # print the moves if specified
        # first get the legal moves for both players as sets
        # this makes them more reusable for after
        # also add any possible captures to the moves
        self.p1legal = self.board.player1.legalMoves(self.board.player2)
        self.p1legal.update(self.board.player1.legalCaptures(self.board.player2))
        self.p2legal = self.board.player2.legalMoves(self.board.player1)
        self.p2legal.update(self.board.player2.legalCaptures(self.board.player1))
        if  verbose:
            # go over all the specified legal moves for both players
            print('PLAYER 1: {}'.format(self.board.player1.color()))
            for move in self.p1legal:
                print('{} --> {}'.format(move[0].pos,move[1]))      
            print('PLAYER 2: {}'.format(self.board.player2.color()))
            for move in self.p2legal:
                print('{} --> {}'.format(move[0].pos,move[1]))
        if showBoard: # print the current state of the board
            print(self.board)
        # now construct the possbile moves arrays
        # this a numpy array object made of tuples wher
        # tuple[0] is current position and tuple[1] is
        # next psoition if the move is performed
        self.p1moves = np.array([(move[0].pos,move[1]) for move in self.p1legal])
        self.p2moves = np.array([(move[0].pos,move[1]) for move in self.p2legal])
        return (self.p1moves.copy(), self.p2moves.copy())
    @staticmethod
    def reward(board, inclOpposite = False):
        """
        Reward function that determines the reward 
        for the current state -- of player1
        the input is a board object
        """
        # check whether there is a winner
        if board.winner() == board.player1:
            return agent.rwin # this meand computer won
        elif board.winner() == board.player2:
            return agent.rloss # computer lost
        # the other state would be when a winner is not decided yet or we have a tie
        result = 0.0
        for piece in board.player1.pieces.values():
            # iterate over the dictionary of board pieces of player1
            # basically, if a piece is on the side which is a more strategic
            # point, give a reward
            if piece.pos[1] == 0 or piece.pos[1] == 0: # if any piece is on the side
                result += agent.rmiddle
            else:
                result += agent.rside
        # I thought maybe I could do the same thing for the opposition board,
        # each opposite side piece has -2.0 and middle ones have -1.0
        # I will keep this optional for testing
        if inclOpposite:
            for piece in board.player1.pieces.values():
                # iterate over the dictionary of board pieces of player2
                if piece.pos[1] == 0 or piece.pos[1] == 0: # if any piece is on the side
                    result += agent.rside
                else:
                    result += agent.rmiddle
        return result
    def policy(self):
        """
        Method that chooses the best next move
        """
        # using the experimentation rate, randomize the next move (or not)
        # use np.random.random that return numbers in [0,1) from a continuous distribution
        # find all the possible legal moves and captures
        legalMoves = self.board.player1.legalMoves(self.board.player2)
        legalMoves.update(self.board.player1.legalCaptures(self.board.player2))
        if np.random.random() < self.expRate:
            print(legalMoves)
    def saveState(self):
        """Save the state of the current board and the action
            leading to it inside the self.states dictionary
        """
        self.states.append()
        pass
