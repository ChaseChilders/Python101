print("Welcome to Chase's Calculator :) ")

number_1 = int(input("Please enter a number: "))

number_2 = int(input("Please enter another number: "))

math_symbol = input("Please enter one of the following: +, -, *, /: ")

def calculator(number_1, number_2, math_symbol):
  if math_symbol == "+":
    print(number_1 + number_2)
  if math_symbol == "_":
    print(number_1 - number_2)
  if math_symbol == "*":
    print(number_1 * number_2)
  if math_symbol == "/":
    print(number_1 / number_2)

  calculator(number_1, number_2, math_symbol)