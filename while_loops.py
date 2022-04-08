# while loop
# count = 0
# while count < 10:
#   #code that will run if the while condition is true
#   print(f'number {count}')
#   count += 1

# # incrementing by 2
# count = 0
# while count < 10: # starts at 0
#   print(f'number {count}')
#   count += 2

# count = 0
# while count < 10:
#   count += 1  # starts at 1
#   print(f'number {count}')

# condition based on user input
# answer = ''
# while answer != 'bye':
#   print('hello')
#   answer = input('') # going to keep going until the user enters 'bye'

# while True: # theres no way this is not true
#   print('Hello') # will print infinitely

# while True:
#   print("""
#   Choose an option:
#   A) Say hello
#   """)
#   user_input = input('')


# number = int(input("Enter a Number: "))
# count = 0
# while count <= number:
#   print (count)
#   count += 1
  
# number = int(input("Enter a number: "))
# another_number = int(input("Enter another number: "))
# while number <= another_number:
#   print (number)
#   number += 1

# number = int(input("Enter a number: "))
# another_number = int(input("Enter another number: "))

# while number <= another_number:
#   if (number % 2) == 1:
#     print(number)
#   number += 1

number = int(input("Enter a number: "))
count = 0
while count <= number:
  count += 1
  if (count % 3) != 0 and (count % 5) != 0:
    print(count)
  elif (count % 3) == 0 and (count % 5) == 0:
    print("fizzbuzz")
  elif (count % 3) == 0:
    print("fizz") 
  elif (count % 5) == 0:
    print("buzz")
  