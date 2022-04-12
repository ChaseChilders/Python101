from flip_coin import flip_coins
from roll_die import roll_dice

def main():
  while True:
    user_input = input("""Please choose an option:
  1 - flip a coin
  2 - roll a die
  q - exit
  """)
    if user_input == "1":
      flip_coins()
    if user_input == "2":
      roll_dice()
    if user_input == "q":
      break