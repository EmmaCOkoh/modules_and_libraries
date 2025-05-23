import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("Dice 1:", dice1)
    print("Dice 2:", dice2)
    print("Total:", dice1 + dice2)

# Call the function
roll_dice()    