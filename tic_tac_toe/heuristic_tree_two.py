import math

class Node:

    def __init__(self, game_state):
        self.game_state = game_state
        self.next_player = self.next_player()
        self.winner = self.check_win_states()
        self.parents = []
        self.children = []
        self.minimax_value = None
        self.depth = 0
    
    def next_player(self):
        next_player = 2
        if self.game_state.count(1) == self.game_state.count(2):
            next_player = 1
        return next_player
    
    def print(self):
         print(f'{self.game_state[0]} {self.game_state[1]} {self.game_state[2]}\n{self.game_state[3]} {self.game_state[4]} {self.game_state[5]}\n{self.game_state[6]} {self.game_state[7]} {self.game_state[8]}')

    def check_win_states(self):

        if self.game_state[0] == self.game_state[1] == self.game_state[2] != 0:
            return self.game_state[0]
        elif self.game_state[3] == self.game_state[4] == self.game_state[5] != 0:
            return self.game_state[3]
        elif self.game_state[6] == self.game_state[7] == self.game_state[8] != 0:
            return self.game_state[6]

        elif self.game_state[0] == self.game_state[3] == self.game_state[6] != 0:
            return self.game_state[0]
        elif self.game_state[1] == self.game_state[4] == self.game_state[7] != 0:
            return self.game_state[1]
        elif self.game_state[2] == self.game_state[5] == self.game_state[8] != 0:
            return self.game_state[2]

        elif self.game_state[0] == self.game_state[4] == self.game_state[8] != 0:
            return self.game_state[0]
        elif self.game_state[2] == self.game_state[4] == self.game_state[6] != 0:
            return self.game_state[2]

        elif 0 not in self.game_state:
            return "Tie"

        return None

    def remaining_moves(self):
    
        avaliable_moves = []
        for i in range(9):
            if self.game_state[i] == 0:
                avaliable_moves.append(i)
        return avaliable_moves

    def assign_minimax_values(self):
        board = self.game_state
        total = 0
        if self.winner != None:
            if self.winner == "Tie":
                return 0
            elif self.winner == 2:
                return -1
            else:
                return self.winner

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

class Queue:
    def __init__(self):
        self.items = []

    def print(self):
        print(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)


class HeuristicTree:
    def __init__(self, ply, root):
        self.ply = ply
        self.root = Node(root)
        self.generate_tree()
        self.assign_minimax_values(self.root)

    def generate_tree(self):
        self.nodes = {}
        self.nodes[tuple(self.root.game_state)] = self.root

        queue = Queue()
        queue.enqueue(self.root)
        while len(queue.items) != 0:

            current_node = queue.items[0]
            queue.dequeue()
            if current_node.depth > self.ply:
                continue

            if current_node.winner == None:
                avaliable_moves = current_node.remaining_moves()
                current_board = current_node.game_state

                for move in avaliable_moves:
                    new_move_board = current_board.copy()
                    new_move_board[move] = current_node.next_player
                    #new_node = Node(new_move_board)

                    if tuple(new_move_board) in self.nodes:
                        new_node = self.nodes[tuple(new_move_board)]
                        current_node.children.append(new_node)
                        new_node.parents.append(current_node)
                        new_node.depth = current_node.depth + 1
                        continue

                    new_node = Node(new_move_board)
                    new_node.depth = current_node.depth + 1
                    new_node.parents.append(current_node)
                    current_node.children.append(new_node)
                    queue.enqueue(new_node)
                    self.nodes[tuple(new_node.game_state)] = new_node

        self.num_nodes = len(self.nodes)

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

# a = HeuristicTree(8, [1, 0, 0, 0, 0, 0, 0, 0, 0])
# print(len(a.nodes))