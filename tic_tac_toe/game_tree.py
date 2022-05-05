class Queue:
    def __init__(self, contents):
        self.line = contents

    def print(self):
        for i in self.line:
            print(i)

    def enqueue(self, item):
        self.line.append(item)

    def dequeue(self):
        return self.line.pop(0)

class Node:
    def __init__(self, board):
        self.state = board
        self.winner = self.check_win()
        if self.winner == None:
            if self.state.count(1) == self.state.count(2):
                self.turn = 1
            else:
                self.turn = 2
        else:
            self.turn = None
        self.children = []
        self.parent = None

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

class TicTacToeTree:
    def __init__(self):
        self.generate_tree()
    
    def generate_tree(self):
        first = Node([0 for i in range(0, 9)])
        queue = Queue([first])

        while len(queue) > 0:
            dequeued = queue.dequeue()

            if dequeued.winner != None:
                continue
                
            board = dequeued.state
            next_player = dequeued.turn
            moves = board.legal_moves(board)
            for move in moves:
                new_board = list(board)
                new_board[move] = next_player
                new_node = Node(new_board)


    def legal_moves(self, board):
        legal = []
        for i in range(0, 9):
            if board[i] == 0:
                legal.append(i)
        return legal

