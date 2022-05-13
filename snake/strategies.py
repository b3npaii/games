def controls(board):
    x = input()
    while x not in ["w", "a", "s", "d"]:
        print("can't do that")
        x = input()
    return x
