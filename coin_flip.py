import random

def coin_flip ():
  click_start = int(input("Type 3 to flip the coin: "))
  flip = random.randint(0,1)
  if click_start == 3:
    if flip == 0:
      print("Heads")
    if flip == 1:
      print("Tails")
  elif click_start != 3:
    print("Type 3 moron ")