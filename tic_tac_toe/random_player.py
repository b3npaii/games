#use 1 dimensional array 9 long for board
import math

class randomPlayer:
    
    def select_move(self, board):
        move = math.random(0, 8)
        while board[move] > 0:
            move = math.random(0, 8)
        return move
