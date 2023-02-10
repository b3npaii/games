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
    def __init__(self, board):
        self.minimax_value = None
        self.state = board
        self.winner = self.check_win()
        if self.winner == None:
            self.turn = 1 if self.state.count(1) == self.state.count(2) else 2
        else:
            self.turn = None
        self.children = []
        self.parents = []
        self.possible_moves = self.find_possible()

    def check_win(self):
        for j in range(3):
            i = 3 * j
            if self.state[j] == self.state[j + 3] == self.state[j + 6] != 0:  # columns
                return self.state[j]
            elif self.state[i] == self.state[i + 1] == self.state[i + 2] != 0:  # rows
                return self.state[i]

        if self.state[0] == self.state[4] == self.state[8] != 0:  # diagonal
            return self.state[4]
        elif self.state[2] == self.state[4] == self.state[6] != 0:  # anti-diagonal
            return self.state[4]
        elif 0 not in self.state:
            return 'Tie'
        
        return None
    
    def legal_moves(self):
        legal = []
        for i in range(0, 9):
            if self.state[i] == 0:
                legal.append(i)
        return legal




class RecombiningTree:
    def __init__(self):
        self.generate_tree()
    
    def generate_tree(self):
        first = Node([0 for i in range(0, 9)])
        queue = Queue([first])
        self.root = first
        seen = {tuple(first.state): first}
        a = 1
        leaves = 0
        terminal = []
        not_terminal = []

        while queue.contents != []:
            dequeued = queue.dequeue()

            # if dequeued.winner is None:
            #     if dequeued not in not_terminal:
            #         not_terminal.append(dequeued)
            # elif dequeued.winner is not None:
            #     if dequeued not in terminal:
            #         if dequeued not in not_terminal:
            #             terminal.append(dequeued)
            if dequeued.winner == 1 or dequeued.winner == 2 or dequeued.winner  == "Tie":
                if dequeued not in terminal and dequeued not in not_terminal:
                    terminal.append(dequeued)
            elif dequeued.winner == None:
                if dequeued not in not_terminal:
                    not_terminal.append(dequeued)
            else:
                if dequeued not in not_terminal:
                    not_terminal.append(dequeued)


            board = dequeued.state
            next_player = dequeued.turn
            moves = dequeued.legal_moves()

            for move in moves:
                a += 1
                new_board = list(board)
                new_board[move] = next_player

                if tuple(new_board) in seen:
                    new_node = seen[tuple(board)]
                    new_node.parents.append(dequeued)
                    dequeued.children.append(new_node)

                else:
                    new_node = Node(new_board)
                    new_node.parents.append(dequeued)
                    dequeued.children.append(new_node)
                    queue.enqueue(new_node)
                    seen[tuple(new_node.state)] = new_node
        self.nodes = seen
        self.terminal_nodes = terminal

a = RecombiningTree()
