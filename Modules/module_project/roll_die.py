from random import randint

def roll_dice():
  dice_sides = int(input("Please select a number of sides for a dice: "))
  roll = randint(1, dice_sides)
  print(roll)