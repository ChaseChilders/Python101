from flip_coin import flip_coins
from roll_die import roll_dice
from roll_multiple_dice import multiple_dice
from random import randint

def main():
  players = int(input("How many players are playing? "))
  selected_player = randint(1, players)
  print(f"Player {selected_player}, it is your turn ")

  while True:
    user_input = input("""Please choose an option:
  1 - flip a coin
  2 - roll a die
  3 - roll multiple die
  q - exit
  """)
    if user_input == "1":
      flip_coins()
    if user_input == "2":
      roll_dice()
    if user_input == "3":
      multiple_dice()
    if user_input == "q":
      break
main()
