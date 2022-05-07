def controls(board):
    x = input()
    while x not in ["w", "a", "s", "d"]:
        print("can't do that")
        x = input()
    return x

class game:
    def __init__(self, strategy):
        self.strat = strategy
        self.board = [[a for i in range(0, 10)] for j in range(0, 10)]
        