import random
from game import *
from heuristic_tree import *

class HeuristicPlayer:
    def __init__(self, ply):
        self.ply = ply

    def choose_move(self, board):
        tree = ConnectFourTree(self.ply, board)
        current_board = tuple([tuple(row) for row in board])
        current_board_node = tree.nodes[current_board]

        minimax_values_of_children = {}
        for child in current_board_node.children:
            tupled_child = tuple([tuple(row) for row in child.state])
            minimax_values_of_children[tupled_child] = child.minimax_value
#get a dictionary of all of the minimax values of the children with the board as the key^

        if current_board_node.next_player == 1:
            board_with_best_move = None
            values_list = list(minimax_values_of_children.values())#all the minimax values of the children
            print(values_list)
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

        for i in range(0, 6):
            for j in range(0, 7):
                if board[i][j] != board_with_best_move[i][j]:
                    return j
                #get the move that makes the current board into the one with the right minimax value

class ManualPlayer:

    def choose_move(self, board): 
        x = input()
        return int(x)

class RandomPlayer:

    def choose_move(self, board):
        legal = []
        for row in range(0, 6):
            for col in range(0, 7):
                if board[row][col] == 0:
                    if col not in legal:
                        legal.append(col)

        return random.choice(legal)
        
class last_minute:

    def choose_move(self, board): 

        self.rows = [board[i] for i in range(len(board))]
        self.columns = [[rows[i] for rows in board] for i in range(7)]

        move = self.check_win_or_block_states(board)

        if move != None: 
            return move

        else: 
            open_columns = self.open_columns(board)
            move = random.choice(open_columns)
            return move

    def check_win_or_block_states(self, board): 
        is_move_posible = False

        for horizontal in self.rows: 
            for i in range(4): 
                #2220
                if horizontal[0 + i] == horizontal[1 + i] == horizontal[2+i] != 0 and horizontal[3+i] == 0: 
                    is_move_posible = True
                    move = 3 + i 
                    return move

                elif horizontal[0 + i] == 0 and horizontal[1 + i] == horizontal[2 + i] == horizontal[3 + i] != 0: 
                    is_move_posible = True
                    move = 0 + i 
                    return move

                elif horizontal[0 + i] == horizontal[1 + i] == horizontal[3 + i] != 0 and  horizontal[2 + i] == 0: 
                    is_move_posible = True
                    move = 2 + i 
                    return move

                elif horizontal[0 + i] == horizontal[2 + i] == horizontal[3 + i] != 0 and  horizontal[1 + i] == 0: 
                    is_move_posible = True
                    move = 1 + i 
                    return move

        for vertical in self.columns: 
            for i in range(3): 
                if vertical[0 + i] == 0 and vertical[1 + i] == vertical[2 + i] == vertical[3 + i] != 0: 
                    is_move_posible = True
                    move = self.columns.index(vertical)
                    return move

        return None

    def open_columns(self, board_copy):
        open_columns = []
        for i in range(7):
            list = [board_copy[j][i] for j in range(len(board_copy))]
            if list.count(list[0]) == len(list) and 0 not in list: 
                continue
            open_columns.append(i)
        return open_columns

        


a = HeuristicPlayer(4)
b = last_minute()

outcomes = {'Tie': 0, 'Player1': 0, 'Player2': 0}
for i in range(0, 10):

    Test = game(b, a)
    player_order = {'Tie': 'Tie', 1: 'Player1', 2: 'Player2'}

    Test.run()
    outcomes[player_order[Test.win]] += 1
print(outcomes)

