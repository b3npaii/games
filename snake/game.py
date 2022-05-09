import random as random

def controls(board):
    x = input()
    while x not in ["w", "a", "s", "d"]:
        print("can't do that")
        x = input()
    return x

class game:
    def __init__(self, strategy):
        self.strat = strategy
        self.board = [["." for i in range(0, 10)] for j in range(0, 10)]
        self.score = 3
        self.snake = [(4, 1), (4, 2), (4, 3)]
        self.berry = None
    
    def generate_berry(self):
        possible_places = []
        for i in range(0, 10):
            for j in range(0, 10):
                if board[i][j] == ".":
                    possible_places.append((i, j))
        self.berry = possible_places[random.randint(0, len(possible_places) - 1)]
    
    def locate_snake(self):
        snake = []
        for i in range(0, 10):
            for j in range(0, 10):
                if self.board[i][j] == 0:
                    snake.append((i, j))
        return snake
    
    

