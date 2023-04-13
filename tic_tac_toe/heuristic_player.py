import random
from game import *
from new_minimax_strat import *
from heuristic_tree_two import *

class HeuristicPlayer:
    def __init__(self, ply):
        self.ply = ply

    def choose_move(self, board):
        tree = HeuristicTree(self.ply, board)
        current_board = tuple(board)
        current_board_node = tree.nodes[current_board]#nodes are stored as tuples in the tree because they're stored as dictionary keys and dictionaries can't have lists as keys

        minimax_values_of_children = {}
        for child in current_board_node.children:
            minimax_values_of_children[tuple(child.game_state)] = child.minimax_value
#get a dictionary of all of the minimax values of the children with the board as the key^

        if current_board_node.next_player == 1:
            board_with_best_move = None
            values_list = list(minimax_values_of_children.values())#all the minimax values of the children
            key_list = list(minimax_values_of_children.keys())#the children boards
            max_value = max(values_list)#max minimax value
            index = values_list.index(max_value)#get the index of the maximum minimax value
            board_with_best_move = key_list[index]#get the board with the highest minimax valueswhy

        elif current_board_node.next_player == 2:
            board_with_best_move = None
            values_list = list(minimax_values_of_children.values())
            key_list = list(minimax_values_of_children.keys())
            min_value = min(values_list)
            index = values_list.index(min_value)
            board_with_best_move = key_list[index]#see above, but with minimum minimax value

        for i in range(0, 9):
            if board[i] != board_with_best_move[i]:
                return i
                #get the move that makes the current board into the one with the right minimax value

class ManualPlayer:

    def choose_move(self, board): 
        x = input()
        return int(x)

class RandomPlayer:

    def choose_move(self, board):
        moves = []
        for i in range(0, len(board)):
            if board[i] == 0:
                moves.append(i)
        return random.choice(moves)


a = HeuristicPlayer(3)
b = MiniMaxStrat()
d = RandomPlayer()
game = Game(b, a)
game.run(log=True)
print(game.check_win())
