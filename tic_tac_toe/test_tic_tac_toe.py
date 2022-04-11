from game import Game
from random_player import randomPlayer
from strategy1 import strat1
"""
player1 = strat1()
player2 = randomPlayer()
outcomes = {'Tie': 0, 1: 0, 2: 0}
for i in range(100000):
    game = Game(player1, player2)
    game.run(log=False)
    outcomes[game.win] += 1
    if i % 1000 == 0:
        print(i)
print(outcomes)
"""
custom_player = strat1()
random_player = randomPlayer()
outcomes = {'Tie': 0, 'custom': 0, 'random': 0}
for i in range(100000):
    if i % 2 == 0:
        game = Game(custom_player, random_player)
        player_order = {'Tie': 'Tie', 1: 'custom', 2: 'random'}
    else:
        game = Game(random_player, custom_player)
        player_order = {'Tie': 'Tie', 1: 'random', 2: 'custom'}

    game.run()
    outcomes[player_order[game.win]] += 1
    if i % 1000 == 0:
        print(i)
print(outcomes)