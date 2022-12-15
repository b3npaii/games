from strategy1 import strat1
from recombining_tree import *
from game import *
from player import Player

class MiniMaxPlayer:
    def __init__(self): 
        tree = TicTacToeRecombiningTree()
        self.nodes = tree.nodes

    def choose_move(self, board):
        
        board_node = self.nodes[tuple(board)]

        children_minimax_values_dict = {tuple(children.game_state) : children.minimax_value for children in board_node.children}

        if board_node.upcoming_player == 1: 
            best_move_board = list(max(children_minimax_values_dict, key=children_minimax_values_dict.get))
        else: 
            best_move_board = list(min(children_minimax_values_dict, key=children_minimax_values_dict.get))
        
        current_board = board_node.game_state

        best_move_index = 0
        for i in range(9): 
            if current_board[i] != best_move_board[i]: 
                best_move_index = i 
                return best_move_index


class ManualPlayer: 
    def choose_move(self, board): 
        x = input()
        return int(x)


Player1 = Player(strat1)

game = Game(MiniMaxPlayer(), MiniMaxPlayer())
game.run(log=True)
print(game.check_win())