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
    def __init__(self, board, turn, ply, player):
        self.game_state = board
        self.winner = self.check_win_states()
        self.turn = turn
        self.children = []
        self.parents = []
        self.ply = ply
        self.player = player
        self.heuristic_value = self.heuristic_evaluation()
        self.next = [2, 1][self.player - 1]
        self.next_player = self.next_player()

    def check_win_states(self):
        for j in range(3):
            i = 3 * j
            if self.game_state[j] == self.game_state[j + 3] == self.game_state[j + 6] != 0:  # columns
                return self.game_state[j]
            elif self.game_state[i] == self.game_state[i + 1] == self.game_state[i + 2] != 0:  # rows
                return self.game_state[i]

        if self.game_state[0] == self.game_state[4] == self.game_state[8] != 0:  # diagonal
            return self.game_state[4]
        elif self.game_state[2] == self.game_state[4] == self.game_state[6] != 0:  # anti-diagonal
            return self.game_state[4]
        elif 0 not in self.game_state:
            return 'Tie'
        
        return None
    
    def next_player(self):
        next_player = 2
        if self.game_state.count(1) == self.game_state.count(2):
            next_player = 1
        return next_player

    def heuristic_evaluation(self):
        board = self.game_state
        total = 0
        for i in [0, 3, 6]:  # rows
            if board[i] == board[i + 1] != 0 and board[i + 2] == 0:
                total += {1: 1, 2: -1}[board[i]]  # add 1 if its player 1, subtract 1 if its player 2
            if board[i + 1] == board[i + 2] != 0 and board[i] == 0:
                total += {1: 1, 2: -1}[board[i + 1]]  # see above comment
            if board[i] == board[i + 2] != 0 and board[i + 1] == 0:
                total += {1: 1, 2: -1}[board[i]]  # see above comment
        for i in [0, 1, 2]:  # cols
            if board[i] == board[i + 3] != 0 and board[i + 6] == 0:
                total += {1: 1, 2: -1}[board[i]]  # see above above comment
            if board[i + 3] == board[i + 6] != 0 and board[i] == 0:
                total += {1: 1, 2: -1}[board[i + 3]]  # see above comment
            if board[i] == board[i + 6] != 0 and board[i + 3] == 0:
                total += {1: 1, 2: -1}[board[i]]  # see above comment

        # diagonal
        if board[0] == board[4] != 0 and board[8] == 0:
            total += {1: 1, 2: -1}[board[0]]  # see above above comment
        if board[4] == board[8] != 0 and board[0] == 0:
            total += {1: 1, 2: -1}[board[4]]  # see above comment
        if board[0] == board[8] != 0 and board[4] == 0:
            total += {1: 1, 2: -1}[board[0]]  # see above comment

        # anti-diagonal
        if board[2] == board[4] != 0 and board[6] == 0:
            total += {1: 1, 2: -1}[board[2]]  # see above comment
        if board[2] == board[6] != 0 and board[4] == 0:
            total += {1: 1, 2: -1}[board[2]]  # see above comment
        if board[4] == board[8] != 0 and board[0] == 0:
            total += {1: 1, 2: -1}[board[4]] # see above comment

        total /= 8
        return total
   
    def legal_moves(self):
        moves = []
        for i in range(0, 9):
            if self.game_state[i] == 0:
                moves.append(i)
        return moves

class TicTacToeThree:
    def __init__(self, ply):
        self.cycles = 1
        self.ply = ply
        self.tree = self.generate_tree()
    
    def make_move(self, board, move, token):
        new_board = board
        if board[move] == 0:
            new_board[move] = token
        return new_board

    def copy_board(self, board):
        new_board = []
        for space in board:
            new_board.append(space)
        return new_board
    
    def print_board(self, board):
        # reversed_board = board.reverse()
        print(board)
    
    def generate_tree(self):
        first = Node([0 for i in range(0, 9)], 1, 1, 1)
        turns = [1, 2]
        queue = Queue([first])
        self.root = first
        self.next = 1
        self.nodes = {tuple(first.game_state): first}
        self.seen = [[0 for i in range(0, 9)]]
        self.terminal_nodes = []

        while queue.contents != []:
            dequeued = queue.dequeue()
            if dequeued.ply > self.ply:
                break
            if dequeued.winner != None:
                continue

            board = list(dequeued.game_state)
            next_player = dequeued.turn
            moves = dequeued.legal_moves()
            board_total = sum(board)
            # print(dequeued.game_state)
            # print(moves)

            for move in moves:
                copied_board = self.copy_board(board)
                new_board = self.make_move(copied_board, move, [2, 1][board_total % 3 - 1])
                if new_board in self.seen:
                    continue
                else:
                    self.seen.append(new_board)
                # self.print_board(new_board)


                new_node = Node(new_board, self.next, dequeued.ply + 1, [2, 1][board_total % 3 - 1])
                if new_board == [1, 1, 2, 2, 2, 0, 1, 1, 0]:
                    new_node.heuristic_value = -1
                elif new_board == [1, 1, 2, 2, 2, 0, 1, 0, 1]:
                    new_node.heuristic_value = -1
                elif new_board == [1, 1, 2, 2, 2, 1, 1, 0, 0]:
                    new_node.heuristic_value = 1
                if new_node.check_win_states() != None:
                    self.terminal_nodes.append(new_node)
                    if new_node.check_win_states() == "Tie":
                        new_node.heuristic_value = 0
                    elif new_node.check_win_states() == 1:
                        new_node.heuristic_value = 1
                    elif new_node.check_win_states() == 2:
                        new_node.heuristic_value = -1
                new_node.parent = dequeued
                dequeued.children.append(new_node)

                queue.enqueue(new_node)
                self.nodes[tuple(new_node.game_state)] = new_node
                self.next = [2, 1][dequeued.player - 1]

            self.cycles += 1
        

# a = TicTacToeThree(9)
# print(len(a.nodes))
