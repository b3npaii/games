from game import Game
from player import Player
from player import random_strat
from strategy1 import strat1
from elias import elias
from jeff import jeff
from celeste import celeste
from christine import christine

Player1 = Player(jeff)
Player2 = Player(christine)

outcomes = {'Tie': 0, 'Player1': 0, 'Player2': 0}
for i in range(100):
    game = Game(Player1, Player2)
    player_order = {'Tie': 'Tie', 1: 'Player1', 2: 'Player2'}

    game.run()
    outcomes[player_order[game.win]] += 1
    if i % 1000 == 0:
        print(i)
print(outcomes)