import random


def diceRoll():
    dice = random.randrange(1, 7)  # a six sided die.
    print(dice)


print('This game will stimulate a dice roll game.\nWith each turn, you will roll a new dice.')
userInput = input('Would you like to play (y/n)?: ')

while 'y' is userInput:
    diceRoll()
    userInput = input('Would you like to play again (y/n)?: ')
else:
    print('Game is finished.')
