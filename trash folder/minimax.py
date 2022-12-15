from recombining_tree import RecombiningTree
from recombining_tree import Queue

class MinimaxStrat:
    def __init__(self):
        self.generateTree()
        self.propogate_values()

    def generateTree(self):
        self.tree = RecombiningTree()
        self.nodes = self.tree.nodes
        self.terminal = self.tree.terminal_nodes

    def propogate_values(self):
        states_to_propogate = Queue()
        for node in self.terminal:
            node.minimax_value = {1: 1, 2: -1, 'Tie': 0}[node.winner]
            for parent in node.parents:
                states_to_propogate.enqueue(parent.state)

        while len(states_to_propogate.contents) > 0:
            state_to_propogate = tuple(states_to_propogate.dequeue())
            current = self.nodes[state_to_propogate]
            minimax_values = []
            for child in current.children:
                # if current.minimax_value == None:
                #     minimax_values.append(0)
                # else:
                minimax_values.append(child.minimax_value)
            print(minimax_values)
            if current.turn == 1:
                current.minimax_value = max(minimax_values)
        #     minimax_values_of_children = []
        #     for child in current.children:
        #         if not hasattr(child, "minimax_value"):
        #             print("hi")
        #             break
        #         minimax_values_of_children.append(child.minimax_value)
        #     print(minimax_values_of_children)
        #     print(current.turn)
        #     if current.turn == 1:
        #         current.minimax_value = max(minimax_values_of_children)
        #     else:
        #         current.minimax_value = min(minimax_values_of_children)

        #     for parent in current.parents:
        #         if hasattr(parent, 'minimax_value') & parent.minimax is not None:
        #             continue
        #         states_to_propogate.enqueue(parent.state)

    def choose_move(self, board):
        board = tuple(board)
        current = self.nodes[board]
        if self.player == 1:
            goal_node = max(current.children, key=lambda node: node.minimax_value)
        else:
            goal_node = min(current.children, key=lambda node: node.minimax_value)
        
        for i in range(0, 9):
            if board[i] != goal_node.state[i]:
                return i

a = MinimaxStrat()
