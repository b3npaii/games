from strategy import Player
from new_strategy import random_strat
from ben_strat import strat_1
from game import game
from jeff_game import *
from jeff_strat import minimaxHeuristic
from celeste_strat import HeuristicPlayer
from elias_strat import *

Player1 = Player(strat_1)
Player2 = Player(random_strat)
Player3 = minimaxHeuristic(1, 4)
Player4 = HeuristicPlayer(4)
Player5 = HeuristicMinimaxStrategy(5, True)


outcomes = {'Tie': 0, 'Player1': 0, 'Player2': 0}
for i in range(4):
    Player3 = minimaxHeuristic(1, 4)

    Test = game(Player5, Player3)
    player_order = {'Tie': 'Tie', 1: 'Player1', 2: 'Player2'}

    Test.run(log=True)
    outcomes[player_order[Test.win]] += 1
    if i % 1000 == 0:
        print(i)
print(outcomes)