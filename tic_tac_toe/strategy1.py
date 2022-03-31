from random import randrange

class strat1:
    def select_move(self, board):
        move = 0
        if board == [0  for _ in range(0, 9)]:
            move =  4
        else:
            move = 2
        return move