from strategy import Player
from strategy import random_strat
from ben_strat import strat_1
from game import game

Player1 = Player(strat_1)
Player2 = Player(random_strat)


outcomes = {'Tie': 0, 'Player1': 0, 'Player2': 0}
for i in range(10000):
    Test = game(Player2, Player1)
    player_order = {'Tie': 'Tie', 1: 'Player1', 2: 'Player2'}

    Test.run()
    outcomes[player_order[Test.win]] += 1
    if i % 1000 == 0:
        print(i)
print(outcomes)