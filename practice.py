# def say_hello():
#   name = input('Hello! what is your name? ')
#   print(f'Hello, {name}!')

# say_hello()

# def how_old():
#   age = input('How old are you? ')
#   print(f'You are {age} years old!')
#   print("Congratulations on making it that far")

# how_old()

# def user_job():
#   occupation = input('What is your occupation? ')
#   print(f"{occupation}, that is a very interesting job")

# user_job()

# Question = input("Do you want to play a Trivia game? ")
# if Question == ("Yes"):
#   print("Very well, let's begin")
# elif Question == ("No"):
#   print("No worries, maybe some other time :)")

# Question2 = input("Who is known as the GOAT of soccer? ")
# if Question2 == ("Lionel Messi"):
#   print("Correct!")
# elif Question2 != ("Lionel Messi"):
#   print("Sorry, that is not correct")

# Question3 = input("What is 42 + 2 - 6? ")
# if Question3 == ("38"):
#   print("You're a math wiz!!")
# elif Question3 != ("38"):
#   print("Oof, not quite")

# user_name = input("What is your name?: ")
# user_age = int(input("How old are you? "))

# till_they_100 = 100 - user_age

# print(f"Hi {user_name}, you have {till_they_100} years until you're 100 :) ")



# def odd_or_even(user_number):
#   if user_number % 2 == 0:
#     print("That is an even number sir :) ")
#   if user_number % 2 == 1:
#     print("That is an odd number sir :) ")

# user_number = int(input("Enter a number here: "))

# odd_or_even(user_number)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for x in a:
#   if x < 5: 
#     print(x)

# print("WELCOME TO ROCK, PAPER, SCISSORS")
# player_1 = input("Player 1, type Rock, Paper, or Scissors: ")
# player_2 = input("Player 2, type Rock, Paper, or Scissors: ")


# def rock_paper_scissors():
#   if player_1 == player_2:
#     print("It's a tie!!!! ")
#   if player_1 == "Rock" and player_2 == "Paper":
#     print("Player 1 is the winner!! ")
#   if player_1 == "Rock" and player_2 == "Scissors":
#     print("Player 1 is the winner")
#   if player_1 == "Rock"

# rock_paper_scissors()\

# number = 0
# while number <= 5:
#   print(number)
#   number += 1

# word = "mississippi"
# for x in  word:
#   print(x)

# def user_number():
#   num_1 = 0
#   while True:
#     user_number = int(input("Please print a number: "))
#     if user_number >= 0:
#       num_1 += 0
#     else:
#       print("The game is over")

# user_number()

# COUNT TO X
# will prompt the user to enter a number and then will count up to that number
# count = 0
# number_1 = int(input("Please enter a number: "))
# while count < number_1:
#   count += 1
#   print(count)

# COUNT N TO M
# will have the user input two numbers and will count up to the second number from the first
# number_1 = int(input("Please select a number: "))
# number_2 = int(input("Please select another number higher than the first: "))
# while number_1 < number_2:
#   number_1 += 1
#   print(number_1)

# COUNT ODD N TO M
# made a program that asks the users for two numbers and it prints only the odd ones in between the two

# # number_1 = int(input("Please enter a number: "))
# # number_2 = int(input("Please select another number: "))
# # while number_1 < number_2:
# #   if (number_1 % 2) == 1:
# #     print(number_1)
# #   number_1 += 1

# # def coin_flip ():
# #   click_start = int(input("Type 3 to flip the coin: "))
# #   flip = random.randint(0,1)
# #   if click_start == 3:
# #     if flip == 0:
# #       print("Heads")
# #     if flip == 1:
# #       print("Tails")
# #   elif click_start != 3:
# #     print("Type 3 moron ")

# import random

# def coin_flip(): 
#   flip = random.randint(0,1)
#   if flip == 0:
#     print('You got heads! ')
#   if flip == 1:
#     print('You got tails!! ')

# # flip = random.randint(0,1)
# #     if flip == 0:
# #       print('You got heads! ')
# #     if flip == 1:
# #       print('You got tails!! ') 

# from ast import While
# import random


# print("Welcome to the coin flipper!")
# print("You have 1 coin. ")
# coins = 1

# def coin_flip():
#   flip = random.randint(0,1)
#   if flip == 0:
#     print("It is Heads! ")
#   if flip == 1:
#     print("It is Tails! ")

# while True:
#   user_input = input("Would you like another?(Say yes or no): ")
#   if user_input == "yes":
#     coins += 1
#     print(f"You have {coins} coins")
#   elif user_input == "no":
#     break
#   else:
#     print("Please print yes or no")

# i = (f"{coins}")

# for i in range(coin_flip):
#   print(f"{i}")
# import random
# target_num, user_input = random.randint(1,10),0

# while target_num != user_input:
#   user_input = int(input("Guess a number between 1 and 9: "))
# if target_num == user_input:
#   print('Well guessed!')
