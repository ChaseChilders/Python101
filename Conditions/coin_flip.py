# import random

# def coin_flip ():
#   click_start = int(input("Type 3 to flip the coin: "))
#   flip = random.randint(0,1)
#   if click_start == 3:
#     if flip == 0:
#       print("Heads")
#     if flip == 1:
#       print("Tails")
#   elif click_start != 3:
#     print("Type 3 moron ")

# import random

# def coin_flip():
#   user_type = input("Type x to flip a coin: ")
#   flip = random.randint(0,1)
#   if user_type == "x":
#     if flip == 1:
#       print("Heads")
#     if flip == 0:
#       print("Tails")

import random
# while True:
#   coin_flip()

# for x in range(5):
#   print(x)
# else: 
#   print("simplilearn")

# def coin_flip():
#   flip = random.randint(0,1)
#   if flip == 0:
#     print("You got heads! ")
#   if flip == 1:
#     print("You got tails ")

# coin_flip()

# user_input = int(input("Enter a number: "))

# def even_or_odd(user_input):
#   if (user_input % 2) == 1:
#     print("It's odd! ")
#   if (user_input % 2) == 0:
#     print("It's even! ")


# even_or_odd(user_input)

user_input = int(input("How many sides should the dice have? (2-20): "))

def dice_roller():
  flip = random.randint(1, user_input)
  print(flip)

dice_roller()