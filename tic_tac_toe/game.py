class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = []
        self.players = [player1, player2]
        for i in range(0, 9):
            self.board.append(0)
        self.next = 1
    
    def print_board
    
    def check_win(self):
        if self.board[0] == self.board[1] == self.board[2] != 0:
            return self.board[1]
        elif self.board[3] == self.board[4] == self.board[5] != 0:
            return self.board[4]
        elif self.board[6] == self.board[7] == self.board[8] != 0:
            return self.board[7]
        elif self.board[0] == self.board[3] == self.board[6] != 0:
            return self.board[0]
        elif self.board[1] == self.board[4] == self.board[7] != 0:
            return self.board[1]
        elif self.board[2] == self.board[5] == self.board[8] != 0:
            return self.board[2]
        elif self.board[1] == self.board[2] == self.board[3] != 0:
            return self.board[1]
        elif self.board[0] == self.board[4] == self.board[8] != 0:
            return self.board[0]
        elif self.board[2] == self.board[4] == self.board[6] != 0:
            return self.board[2]
        elif 0 not in self.board:
            return "tie"
        return None
    
    def valid_move(self, move):
        if self.board[move] != 0:
            return False
        else:
            return True
    
    def make_move(self):
        current_player = self.players[self.next - 1]
        move = current_player.select_move(self.board)
        if self.valid_move(move) == True:
            self.board[move] = self.next
        if self.log == True:

    
    #def run(self, log=False):
        #self.log = log

     