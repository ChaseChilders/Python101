from random import randint

def multiple_dice():
  dice = int(input("How many dice would you like to roll? "))
  dice_sides = int(input("Hoe many sides would you like your dice to have? "))
  all_sides_roll = dice_sides * dice
  final = randint(1, all_sides_roll)
  print(final)