from heuristic_tree import *
from recombining_tree import *

a = TicTacToeThree(9)
akeys = a.nodes
b = TicTacToeRecombiningTree()
bkeys = b.nodes.keys
i = 0
for akey in akeys:
    if a.nodes[tuple(akey)].heuristic_value > 0  and b.nodes[tuple(akey)].minimax_value > 0:
        continue
    elif a.nodes[tuple(akey)].heuristic_value < 0 and b.nodes[tuple(akey)].minimax_value < 0:
        continue
    elif a.nodes[tuple(akey)].heuristic_value == b.nodes[tuple(akey)].minimax_value == 0:
        continue
    else:
        print(a.nodes[akey].game_state)
        print(a.nodes[akey].heuristic_value)
        print(b.nodes[akey].game_state)
        print(b.nodes[akey].minimax_value)
        print()
        i += 1
print(i)
print(a.nodes[(1, 1, 2, 2, 2, 1, 1, 0, 0)].heuristic_value)