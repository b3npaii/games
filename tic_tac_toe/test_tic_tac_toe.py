from game import Game
from player import Player
from player import random_strat
from strategy1 import strat1
from elias import strategy
from jeff import jeff

Player1 = Player(strat1)
Player2 = Player(jeff)
outcomes = {'Tie': 0, 'custom': 0, 'random': 0}
for i in range(100000):
    if i % 2 == 0:
        game = Game(Player1, Player2)
        player_order = {'Tie': 'Tie', 1: 'custom', 2: 'random'}
    else:
        game = Game(Player1, Player2)
        player_order = {'Tie': 'Tie', 1: 'random', 2: 'custom'}

    game.run()
    outcomes[player_order[game.win]] += 1
    if i % 1000 == 0:
        print(i)
print(outcomes)