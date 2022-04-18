class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = []
        self.players = [player1, player2]
        for i in range(0, 9):
            self.board.append(0)
        self.next = 1
        
    
    def print_board(self):
        print(self.board[:3])
        print(self.board[3:6])
        print(self.board[6:9])
    
    def check_win(self):
        for j in range(3):
            i = 3 * j
            if self.board[j] == self.board[j + 3] == self.board[j + 6] != 0:  # columns
                return self.board[j]
            elif self.board[i] == self.board[i + 1] == self.board[i + 2] != 0:  # rows
                return self.board[i]

        if self.board[0] == self.board[4] == self.board[8] != 0:  # diagonal
            return self.board[4]
        elif self.board[2] == self.board[4] == self.board[6] != 0:  # anti-diagonal
            return self.board[4]
        elif 0 not in self.board:
            return 'Tie'
        
        return None
    
    def valid_move(self, move):
        if self.board[move] == 0:
            return True
        else:
            return False
    
    def make_move(self):
        current_player = self.players[self.next - 1]
        move = current_player.choose_move(self.board)
        if type(move) is tuple:
            move = list(move)
            move = move[0] * 3 + move[1]
        if self.valid_move(move) == True:
            self.board[move] = self.next
        if self.log == True:
            print()
            self.print_board()
            print('Move was', move, 'made by', self.next)
            print()
        self.next = [2, 1][self.next - 1]
    
    def run(self, log=False):
        self.log = log
        self.win = self.check_win()
        while self.win == None:
            self.make_move()
            self.win = self.check_win()