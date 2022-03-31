from game import Game
from random_player import randomPlayer

player1 = randomPlayer()
player2 = randomPlayer()
outcomes = {'tie': 0, 1: 0, 2: 0}
for i in range(10000):
    game = Game(player2, player1)
    game.run(log=False)
    # print(game.winner)
    outcomes[game.win] += 1
    if i % 1000 == 0:
        print(i)
print(outcomes)