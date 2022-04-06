# assignment operator =
from re import L


dog = 'Nelson' # assigning value "kobe" to variable 'dog'
introduction = "Kobe's name is Kobe" #single and double quotes
# introduction = 'nelson's name is nelson' doesn't work because it uses single quotes
# string containing single quotes needs double quotes

# strings with both need multiple quotes
introducton = """Nelson's name is "nelson" """
#characters can be escaped using backslash
introduction = "my dog's name is \"nelson\""

#multi-line strings
#use triple quotes to use new lines
long_introduction = """
hello

my dog's name is "Nelson"
"""
#use escaped newline \n is a new line character
long_introduction = "hello\n\nmy dog's name is \"nelson\""

# passing variables to a function as an argument
#print(dog)

#print(long_introduction)

# string concatenation
#new_introduction = "my dog's  name is " + dog + " he is awesome!"
#print(new_introduction)
#dog = "toby"
#new_introduction = "my dog's  name is " + dog + " he is awesome!"
#print(new_introduction)

#accessing the 1st-5th letter in the value user details [0:10], [10:]
# user_details = 'password: helloworld!123'
# print(user_details[10:])

# User Greeter
firstName = "Chase"
lastName = "Childers"

print("Hello " + firstName + ' ' + lastName)

# Email Generator
print(firstName[0] + '.' + lastName + "@gmail.com")

# Username Generator
print(firstName[0:3] + "_" + lastName)

# New User Contact Information
print("Welcome to Digital Crafts, " + firstName + ' ' + lastName + "!")
print("Email: " + firstName[0] + "." + lastName + "@gmail.com")
print("Username: " + firstName[0:3] + "_" + lastName[0:5])

# f-string format
print(f"Hello, {firstName} {lastName}.")

print(f"{firstName[0]}.{lastName}@gmail.com")

print(f"Welcome to Digital Crafts, {firstName} {lastName}!")