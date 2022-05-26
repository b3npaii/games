import random as random
from strategies import controls
from ben_strat import Ben
from ben_strat import strat2
from elias import elias
from celeste import celeste

class game:
    def __init__(self, player):
        self.player = player
        self.board = [[" " for i in range(0, 10)] for j in range(0, 10)]
        self.score = 3
        self.snake = [(4, 1), (4, 2), (4, 3)]
        self.berry = None
        self.moves = 0
    
    def generate_berry(self):
        possible_places = []
        for i in range(0, 10):
            for j in range(0, 10):
                if self.board[i][j] == " ":
                    possible_places.append((i, j))
        self.berry = possible_places[random.randint(0, len(possible_places) - 1)]
    
    def locate_snake(self):
        snake = []
        for i in range(0, 10):
            for j in range(0, 10):
                if self.board[i][j] == "O":
                    snake.append((i, j))
        return snake
    
    def check_collision(self):
        if len(list(set(self.snake))) != len(self.snake):
            return True
        elif self.snake[-1][0] not in range(0, 10):
            return True
        elif self.snake[-1][1] not in range(0, 10):
            return True
        return False
    
    def make_move(self):
        self.moves += 1
        move = self.player.choose_move(self, self.board)
        return move
    

    def game(self):
        self.generate_berry()
        while True:
            for i in range(0, 10):
                for j in range(0, 10):
                    self.board[i][j] = " "
            self.board[self.berry[0]][self.berry[1]] = "b"
            for part in self.snake[:-1]:
                self.board[part[0]][part[1]] = "O"
            self.board[self.snake[-1][0]][self.snake[-1][1]] = "e"
#            for row in self.board:
#                print(row)
            move = self.make_move()
            new_segment = None
            if move == 'w':
                new_segment = (self.snake[-1][0] - 1, self.snake[-1][1])
            elif move == 's':
                new_segment = (self.snake[-1][0] + 1, self.snake[-1][1])
            elif move == 'a':
                new_segment = (self.snake[-1][0], self.snake[-1][1] - 1)
            elif move == 'd':
                new_segment = (self.snake[-1][0], self.snake[-1][1] + 1)
            self.snake.append(new_segment)
            if self.check_collision() == True:
                print(self.score - 3)
                return self.score - 3
            if self.score == 99:
                self.score = 97
                return
            self.snake = self.snake[-self.score:]
            if self.berry in self.snake:
                self.score += 1
                self.generate_berry()
totals = {'score': 0, 'moves': 0}
for i in range(100):
    bruh = game(elias)
    result = bruh.game()
    totals['score'] += bruh.score
    totals['moves'] += bruh.moves
    if i % 100 == 0:
        print(i)

averages = {'score': totals['score'] / 100, 'moves': totals['moves'] / 100}
print(averages)