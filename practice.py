def say_hello():
  name = input('Hello! what is your name? ')
  print(f'Hello, {name}!')

say_hello()

def how_old():
  age = input('How old are you? ')
  print(f'You are {age} years old!')
  print("Congratulations on making it that far")

how_old()

def user_job():
  occupation = input('What is your occupation? ')
  print(f"{occupation}, that is a very interesting job")

user_job()

Question = input("Do you want to play a Trivia game? ")
if Question == ("Yes"):
  print("Very well, let's begin")
elif Question == ("No"):
  print("No worries, maybe some other time :)")

Question2 = input("Who is known as the GOAT of soccer? ")
if Question2 == ("Lionel Messi"):
  print("Correct!")
elif Question2 != ("Lionel Messi"):
  print("Sorry, that is not correct")

Question3 = input("What is 42 + 2 - 6? ")
if Question3 == ("38"):
  print("You're a math wiz!!")
elif Question3 != ("38"):
  print("Oof, not quite")