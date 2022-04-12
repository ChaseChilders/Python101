# # print("Hello")
# # name = input("What is your name?")

# # # # if the name is "Nelson"
# # if name == "Nelson":
# #   print("You're cool")

# # # # combining conditions
# # if name == "Nelson" or name != "Angel":
# #   print("You suck")

# # if name != "Nelson":
# #   print("You're not cool")

# # name = "Steve"
# # print(name == "Nelson") #this prints false

# # age = int(input("What is your age? "))
# # if age < 21:
# #   print("You cannot enter this establishment")

# # if age >= 21:
# #   print('Come on in!')

# # age = int(input("What is your age? "))
# # if age < 21:
# #   print("You cannot enter this establishment")

# # else:
# #   print('Come on in!')


# choice = input ("""
# Choose an option:
# A) say hello
# B) do a dance
# C) do nothing
# """)

# if choice == 'A':
#   print('HAI')
# elif choice == 'B'
#   print('Yes')
# elif choice == 'C'
#   print('...')
# else:
#   print('Wrong')


# num = int(input('pick a number'))

# if num > 5 and num < 10:
#   print('ok, bigger than 5')

# elif num > 10 and num <= 9000:
#   print('getting bigger')

# elif num > 9000:
#   print("That's absurd")

# day of the week

# day = input('pick a day of the week ')

# if day == ("Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday"):
#   print('go to work!')

# elif day == ("Saturday" or "Sunday"):
#   print('Sleep in!')

# else:
#   print("enter a valid day")

#password

# password = input('What is the password? ')

# if password == ("Digital"):
#   print("Welcome")

# else:
#   print("Try Again")

# Day of the week

# dayOfWeek = int(input("Pick a number between 1-7 "))
# if dayOfWeek == 1:
#   print("Monday")
# elif dayOfWeek == 2:
#   print("Tuesday")
# elif dayOfWeek == 3:
#   print("Wednesday")
# elif dayOfWeek == 4:
#   print("Thursday")
# elif dayOfWeek == 5:
#   print("Friday")
# elif dayOfWeek == 6:
#   print("Saturday")
# elif dayOfWeek == 7:
#   print("Sunday")
# else:
#   print("Error")

# Letter Grade

# letterGrade = int(input('Enter a score 1-100 '))
# if letterGrade < 60:
#   print("F")
# elif letterGrade < 70 and letterGrade >= 60:
#   print("D")
# elif letterGrade <80 and letterGrade >= 70:
#   print("C")
# elif letterGrade <90 and letterGrade >= 80:
#   print("B")
# elif letterGrade <= 100 and letterGrade >= 90:
#   print("A")
# else:
#   print("Enter a valid score")

def same_letter(input1, input2):
  if (input1[0]) == (input2[0]):
    print("You can come to the party")
  else:
    print("Try again")

input1 = input("What is your name? ")
input2 = input("What food are you bringing to the picnic? ")

same_letter(input1, input2)