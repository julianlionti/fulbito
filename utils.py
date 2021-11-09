from random import randrange


def randomZeroOne():
    rand = randrange(0, 100)
    zeroOne = rand / 100
    if zeroOne > 0.49:
        return 1
    else:
        return 0
