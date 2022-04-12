# single number dice roller

import random

print("Lets roll a dice! ")
dice_sides = int(input("Print a number between 2 and 20: "))

def function (dice_sides):
  roll = random.randint(1, dice_sides)
  print(roll)

function(dice_sides)

# dice roller between two user inputs

number_1 = int(input("Pick a number: "))
number_2 = int(input("Pick another number higher than the last one: "))

def dice_roller(number_1, number_2):
  if number_1 < number_2:
    random.randint(number_1, number_2)
    dice_number = random.randint(number_1, number_2)
    print(dice_number)

dice_roller(number_1, number_2)