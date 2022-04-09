# names = ['bruce', 'peter', 'steve', 'tchala', 'tony']

# for name in names:
#   print('hello ' + name)


# word = input('enter a word: ')
# print('how to spell: ' + word)

# for character in word:
#   print('put a letter ' + character + ' on the page')

# loop over a range

# for i in range(10): #range is assigning index values
#   print(i)

# # 
# num1 = int(input('number 1: '))
# num2 = int(input('number 2: '))

# for number in range(num1, num2 + 1):
#   print(number)


# # clock (nested loop)
# for hour in range(24):
#   for minute in range (60):
#     print(f"{hour}:{minute}")

# for i in range(5):
#   print('*****')

# height = int(input("How tall would you like your pyramid: ")) 

# for i in range(height):
#   spaces = height - 1 - i
#   stars = i * 2 + 1
#   print(" " * spaces + "*" * stars)

# range(5, 10) # will print 5, 6, 7, 8, 9

# for number_1 in range(1, 11):
#   for number_2 in range(1, 11):
#     answer = number_1 * number_2
#     print (f"{number_1} * {number_2} = {answer}")

# pseudo code
# ask for input height
# ask for input width
# start loop for row in height
    # test that the row loop works
    # print '.'
    # first is same as last so if row is first or last
    # if (i == 0):
    #   #print stars for total width
    #   print('*' * width)
    # insides are all the same
      # print star then (width - 2) spaces, then star


height = int(input("Height: ")) 
width = int(input("Width: "))

for i in range(height):

  if (i == 0) or i == height - 1:

    print('*' * width)
  else: 
    print('*' + ' ' *  (width - 2) + '*' )
