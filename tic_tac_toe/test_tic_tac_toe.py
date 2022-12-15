from game import Game
from player import Player
from player import random_strat
from strategy1 import strat1
from elias import elias
from jeff import jeff
from celeste import celeste
from christine import christine
from minimax import MinimaxStrat


Player1 = MinimaxStrat()
Player2 = MinimaxStrat()

outcomes = {'Tie': 0, 1: 0, 2: 0}
for i in range(1000):
    game = Game(Player1, Player2)
    game.run()
    outcomes[game.winner] += 1
print(outcomes)