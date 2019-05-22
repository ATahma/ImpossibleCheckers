# player class for SAM checkers
class player:
    def __init__(self, color):
        """define a new computer player"""
        self.color = color
    def returnColor(self):
        """REturn a copy of the color of the current player"""
        return self.color[:]
    def moveList(self):
        """Calcualte or return all the possible moves 
        for this player at this point"""
        # TO DO
        return None
    def movePiece(self):
        """Function that orders the best move to be taken"""
    
