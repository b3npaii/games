from game import Game
from player import Player
from player import random_strat
from strategy1 import strat1
from elias import elias
from jeff import jeff
from celeste import celeste
from christine import christine

Player1 = Player(strat1)
Player2 = Player(random_strat)

outcomes = {'Tie': 0, 'Player1': 0, 'Player2': 0}
for i in range(10000):
    game = Game(Player2, Player1)
    player_order = {'Tie': 'Tie', 1: 'Player1', 2: 'Player2'}

    game.run()
    outcomes[player_order[game.win]] += 1
    if i % 1000 == 0:
        print(i)
print(outcomes)