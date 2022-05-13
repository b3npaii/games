class game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = []
        self.players = [player1, player2]
        row = [0 for i in range(0, 7)]
        for i in range(0, 6):
            self.board.append(board)
        self.next = 1
    
    def valid_moved(self, move):
        for row in self.board:
            if row[move] == 0:
                return True

    def print_board(self):
         for row in reversed(self.board):
             print(row)

    def check_winner(self):
        if self.board == [[0 for _ in range(7)] for _ in range(6)]:
            return None
        player_that_made_move = self.previous_player
        for i in range(0, 6):
            for j in range(0, 4):
                print(j)
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
