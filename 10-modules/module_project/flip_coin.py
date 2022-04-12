from random import randint

def flip_coins():
  flip = randint(0,1)
  if flip == 0:
    print("HEADS")
  if flip == 1:
    print("TAILS")