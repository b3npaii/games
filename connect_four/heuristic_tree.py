def calc_minimum(numbers):
    a = numbers[0]
    for number in numbers:
        if number < a:
            a = number
    return a

def simple_sort(numbers):
    answer_arr = []
    for number in numbers:
        while len(numbers) > 0:
            value = calc_minimum(numbers)
            answer_arr.append(value)
            numbers.remove(value)
    return answer_arr

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
        self.turn = self.next()
        self.children = []
        self.parent = None
        self.ply = ply
        self.minimax_value = self.assign_minimax_values()
        self.next_player = self.next()
    
    def next(self):
        board = self.state
        total = 0
        for row in board:
            for space in row:
                total += space
        if total % 3 == 1:
            return 2
        elif total % 3 == 0:
            return 1

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
        return simple_sort(legal)

    def assign_minimax_values(self): 
        board = self.state
        total = 0
        checks = 0

        if self.winner != None:
            if self.winner == "Tie":
                return 0
            elif self.winner == 2:
                return -100000
            else:
                return 100000

        for i in range(0, 4):
            for j in range(0, 5):
                if board[j][i] == board[j][i + 1] == board[j][i + 2] != 0 and board[j][i + 3] == 0:
                    total += {1: 1, 2: -1}[board[j][i]]

                elif board[j][i] == 0 and board[j][i + 1] == board[j][i + 2] == board[j][i + 3] != 0:
                    total += {1: 1, 2: -1}[board[j][i + 1]]

                elif board[j][i] == board[j][i + 2] == board[j][i + 3] != 0 and board[j][i + 1] == 0:
                    total += {1: 1, 2: -1}[board[j][i]]

                elif board[j][i] == board[j][i + 1] == board[j][i + 3]!= 0 and board[j][i + 2] == 0:
                    total += {1: 1, 2: -1}[board[j][i]]


        for i in range(0, 3):
            for j in range(0, 6):
                if board[i][j] == board[i + 1][j] == board[i + 2][j] != 0 and board[i + 3][j] == 0:
                    total += {1: 1, 2: -1}[board[i][j]]

                elif board[i][j] == 0 and board[i + 1][j] == board[i + 2][j] == board[i + 3][j] != 0:
                    total += {1: 1, 2: -1}[board[i + 1][j]]

                elif board[i + 1][j] == 0 and board[i][j] == board[i + 2][j] == board[i + 3][j] != 0:
                    total += {1: 1, 2: -1}[board[i][j]]

                elif board[i + 2][j] == 0 and board[i][j] == board[i + 1][j] == board[i + 3][j] != 0:
                    total += {1: 1, 2: -1}[board[i][j]]
        
        for i in range(0, 3):
            for j in range(0, 4):
                if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] != 0 and board[i + 3][j + 3] == board[i + 2][j + 3] == 0:
                    total += {1: 1, 2: -1}[board[i][j]]

                elif board[i][j] == board[i - 1][j] == 0 and board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] != 0:
                    total += {1: 1, 2: -1}[board[i + 1][j + 1]]

                elif board[i][j] == board[i + 3][j + 3] == board[i + 2][j + 2] != 0 and board[i + 1][j + 1] == board[i][j + 1] == 0:
                    total += {1: 1, 2: -1}[board[i][j]]

                elif board[i][j] == board[i + 1][j + 1] == board[i + 3][j + 3] != 0 and board[i + 2][j + 2] == board[i + 1][j + 2] == 0:
                    total += {1: 1, 2: -1}[board[i][j]]

        for i in range(0, 3):
            for j in [6, 5, 4, 3]:
                if board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] != 0 and board[i + 3][j - 3] == board[i + 2][j - 3] == 0:
                    total += {1: 1, 2: -1}[board[i][j]]
                
                elif board[i][j] == board[i + 1][j - 1] == board[i + 3][j - 3] != 0 and board[i + 2][j - 2] == board[i + 1][j - 2] == 0:
                    total += {1: 1, 2: -1}[board[i + 1][j - 1]]

                elif board[i][j] == board[i + 3][j - 3] == board[i + 2][j - 2] != 0 and board[i + 1][j - 1] == board[i][j - 1] == 0:
                    total += {1: 1, 2: -1}[board[i][j]]

                elif board[i + 3][j - 3] == board[i + 1][j - 1] == board[i + 2][j - 2] != 0 and board[i][j] == board[i - 1][j] == 0:
                    total += {1: 1, 2: -1}[board[i + 3][j - 3]]

        return total

class ConnectFourTree:
    def __init__(self, ply, board):
        self.cycles = 1
        self.ply = ply
        self.tree = self.generate_tree(board)
        self.assign_minimax_values(Node(board, 1, 1))

    def make_move(self, board, column):
        for row in range(0, 6):
            if board[row][column] == 0:
                board[row][column] = self.next_player(board)
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
    
    def next_player(self, board):
        total = 0
        for row in board:
            for space in row:
                total += space
        if total % 3 == 1:
            return 2
        elif total % 3 == 0:
            return 1

    def generate_tree(self, board):
        first = Node(board, 1, 1)
        turns = [1, 2]
        queue = Queue([first])
        self.root = first
        self.next = 1

        self.nodes = {tuple([tuple(row) for row in board]): first}

        while queue.contents != []:
            dequeued = queue.dequeue()
            if dequeued.ply > self.ply:
                break
            if dequeued.winner != None:
                continue

            board = dequeued.state
            next_player = self.next_player(board)
            moves = dequeued.legal_moves()
            list_of_nodes = []

            for move in moves:
                copied_board = self.copy_board(board)
                new_board = self.make_move(copied_board, move)
                tupled_board = tuple([tuple(row) for row in new_board])


                new_node = Node(new_board, self.next, dequeued.ply + 1)
                # self.print_board(new_node.state)
                # print(new_node.assign_minimax_values())
                # print()
                new_node.parent = dequeued
                dequeued.children.append(new_node)

                list_of_nodes.append(new_node)
                self.nodes[tupled_board] = new_node


            for node in list_of_nodes:
                queue.enqueue(node)

            self.next = [2, 1][self.next - 1]
            self.cycles += 1
    
    def assign_minimax_values(self, node):

        if node.children == []:
            node.minimax_value = node.assign_minimax_values()

        else:
            children_minimax_values = []

            for child in node.children:
                self.assign_minimax_values(child)
                children_minimax_values.append(child.minimax_value)

            if node.next_player == 1:
                node.minimax_value = max(children_minimax_values)
            else:
                node.minimax_value = min(children_minimax_values)

        return node.minimax_value
#it's not making new nodes right now, just editing the same one a bunch of times



# tree = ConnectFourTree(6)
