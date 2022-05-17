class game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = []
        self.players = [player1, player2]
        row = [0 for i in range(0, 7)]
        for i in range(0, 6):
            self.board.append(row)
        self.next = 1
    
    def valid_move(self, move):
        for row in self.board:
            if row[move] == 0:
                return True
        return False

    def check_winner(self):
        if self.board == [[0 for _ in range(7)] for _ in range(6)]:
            return None
        player_that_made_move = self.previous
        for i in range(0, 6):
            for j in range(0, 4):
                if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] == self.board[i][j + 3] != 0:
                    return self.board[i][j]
        for i in range(0, 3):
            for j in range(0, 7):
                if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] == self.board[i + 3][j] != 0:
                    return self.board[i][j]
        for i in range(0, 3):
            for j in range(0, 4):
                if self.board[i][j] == self.board[i + 1][j + 1] == self.board[i + 2][j + 2] == self.board[i + 3][j + 3] != 0:
                    return self.board[i][j]
                elif self.board[5 - i][j] == self.board[5 - (i + 1)][j + 1] == self.board[5 - (i + 2)][j + 2] == self.board[5 - (i + 3)][j + 3] != 0:
                    return self.board[i][j]
        if any(0 in row for row in self.board):
            pass
        else:
            return 'Tie'
        return None
    
    def gravity(self, player, column):
        for row in self.board:
            if row[column] == 0:
                self.board[self.board.index(row)][column] = player 
                break
    
    def make_move(self):
        current = self.players[self.next - 1]
        move = current.choose_move(self.board)
        if self.valid_move(move) == True:
            self.gravity(self.next, move)
            self.previous = self.next
        if self.log == True:
            for row in reversed(self.board):
                print(row)
            print()
        self.next = [2, 1][self.next - 1]

    def run(self, log=False):
        self.log = log
        self.win = self.check_winner()
        while self.win == None:
            self.make_move()
            self.win = self.check_winner()

from strategy import RandomPlayer

a = RandomPlayer()
b = RandomPlayer()

game = game(a, b)
game.run(log=True)
print('winner: ', game.win)

