# input accepts user input and returns that value as a string
# it can be stored in a variable and used later

# name = input('What is your name? ')
# print(f'Hello {name}!')

# defining function
# def say_hello():
#   name = input('What is your name? ')
#   print(f'Hello, {name}!')

# def my_dog(name, age):
#   print(f"My dog's name is {name} and he is {age} yuears old")

# #say_hello()
# my_dog("Nelson", 16)
# my_dog("Bongo", 13)

def say_hi(first_name, last_name):
  print(f"Top of the morning to you, {first_name} {last_name}!")

# say_hi("Michael", "Jordan")
# say_hi("Dennis", "Rodman")

def user_email(first_name, last_name, domain):
  print(f"{first_name[0]}.{last_name[0:5]}{domain}")

# user_email("chase", "childers", "@gmail.com")

def user_name(first_name, last_name):
  print(f"{first_name[0:3]}_{last_name[0:5]}")

# user_name("Chase", "Childers")

# def contact_card(first_name, last_name, domain):
#   print(f"Top of the morning to you, {first_name} {last_name}!")
#   print("Email:")
#   print(f"{first_name[0]}.{last_name[0:5]}{domain}")
#   print("Username:")
#   print(f"{first_name[0:3]}_{last_name[0:5]}")

# contact_card("Chase", "Childers", "@gmail.com")

def contact_card(first_name, last_name, domain):
  say_hi(first_name, last_name)
  print("Email:")
  user_email(first_name, last_name, domain)
  print("Username:")
  user_name(first_name, last_name)

contact_card("Chase", "Childers", "@gmail.com")
