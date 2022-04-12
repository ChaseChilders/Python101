def even_odd():
  enter_number = int(input("Enter a number: "))
  if (enter_number % 2) == 1:
    print("It's Odd!! ")
  if (enter_number % 2) == 0:
    print("It's Even!! ")
  else: 
    print("Enter a valid number: ")

while True:
  even_odd()