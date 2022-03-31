from game import Game
from random_player import randomPlayer
from strategy1 import strat1

player1 = strat1()
player2 = randomPlayer()
outcomes = {'Tie': 0, 1: 0, 2: 0}
for i in range(100000):
    game = Game(player2, player1)
    game.run(log=False)
    outcomes[game.win] += 1
    if i % 1000 == 0:
        print(i)
print(outcomes)
