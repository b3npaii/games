#use 1 dimensional array 9 long for board
from random import randrange

class randomPlayer:
    
    def select_move(self, board):
        move = randrange(0, 9)
        while board[move] != 0:
            move = randrange(0, 9)
        return move
