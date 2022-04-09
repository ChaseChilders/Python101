import random

print("Lets roll a dice! ")
dice_sides = int(input("Print a number between 2 and 20: "))

def function (dice_sides):
  roll = random.randint(1, dice_sides)
  print(roll)

function(dice_sides)