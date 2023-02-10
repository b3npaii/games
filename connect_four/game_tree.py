class Queue:
    def __init__(self, contents=None):
        if contents is None:
            self.contents = []
        else:
            self.contents = contents
    def print(self):
        for item in self.contents:
            print(item)
    def enqueue(self, item_to_queue):
        self.contents.append(item_to_queue)
    def dequeue(self):
        return self.contents.pop(0)

class Node:
    def __init__(self, board, turn, ply):
        self.state = board
        self.winner = self.check_winner()
        self.turn = turn
        self.children = []
        self.parent = None
        self.ply = ply

    def check_winner(self):
        if self.state == [[0 for _ in range(7)] for _ in range(6)]:
            return None
        for i in range(0, 6):
            for j in range(0, 4):
                if self.state[i][j] == self.state[i][j + 1] == self.state[i][j + 2] == self.state[i][j + 3] != 0:
                    return self.state[i][j]
        for i in range(0, 3):
            for j in range(0, 7):
                if self.state[i][j] == self.state[i + 1][j] == self.state[i + 2][j] == self.state[i + 3][j] != 0:
                    return self.state[i][j]
        for i in range(0, 3):
            for j in range(0, 4):
                if self.state[i][j] == self.state[i + 1][j + 1] == self.state[i + 2][j + 2] == self.state[i + 3][j + 3] != 0:
                    return self.state[i][j]
                elif self.state[5 - i][j] == self.state[5 - (i + 1)][j + 1] == self.state[5 - (i + 2)][j + 2] == self.state[5 - (i + 3)][j + 3] != 0:
                    return self.state[i][j]
        if any(0 in row for row in self.state):
            pass
        else:
            return 'Tie'
        return None
    
    def legal_moves(self):
        legal = []
        for row in range(0, 6):
            for col in range(0, 7):
                if self.state[row][col] == 0:
                    if col not in legal:
                        legal.append(col)
        return legal

class ConnectFourTree:
    def __init__(self, ply):
        self.cycles = 1
        self.ply = ply
        self.tree = self.generate_tree()
    
    def make_move(self, board, column):
        for row in range(0, 6):
            if board[row][column] == 0:
                board[row][column] = self.next
                return board

    def copy_board(self, board):
        new_board = []
        for row in board:
            new_row = []
            for col in row:
                new_row.append(col)
            new_board.append(new_row)
        return new_board
    
    def print_board(self, board):
        # reversed_board = board.reverse()
        for row in board:
            print(row)
        print()
    
    def generate_tree(self):
        first = Node([[0 for _ in range(7)] for _ in range(6)], 1, 1)
        turns = [1, 2]
        queue = Queue([first])
        self.root = first
        self.next = 1
        self.nodes = [first]

        while queue.contents != []:
            dequeued = queue.dequeue()
            if dequeued.ply > self.ply:
                break
            if dequeued.winner != None:
                continue

            board = dequeued.state
            next_player = dequeued.turn
            moves = dequeued.legal_moves()
            list_of_nodes = []

            for move in moves:
                # print(self.next)
                copied_board = self.copy_board(board)
                new_board = self.make_move(copied_board, move)
                # self.print_board(new_board)

                new_node = Node(new_board, self.next, dequeued.ply + 1)
                new_node.parent = dequeued
                dequeued.children.append(new_node)

                list_of_nodes.append(new_node)
                self.nodes.append(new_node)

            for node in list_of_nodes:
                queue.enqueue(node)

            self.next = [2, 1][self.next - 1]
            self.cycles += 1
#it's not making new nodes right now, just editing the same one a bunch of times


for i in range(1, 5):
    tree = ConnectFourTree(i)
    print(str(i))
    print(len(tree.nodes))