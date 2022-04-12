# types we've seen so far: string, number (floats and integers), boolean (true or false)
# new type: list

# empty list
names = []

#list of strings
names = ['tony', 'steve', 'tchala']

# list of integers
numbers = [2, 4, 6, 8, 9]

# list of mixed values
weird = ['pancakes', 10, True]

# access items with index inside square brackets
# print (names[1])

# print(weird[3]) # index error (out of range)
# print(numbers[1:4])

# #change value at specific position
# names = ['tony', 'steve', 'tchala']
# names[0] = 'Peter' #changed tony to peter
# names.append('tony') # added tony to end of list
# names.insert(0, 'bruce') # inserted bruce at beggining
# names.pop() # removes the last index of the list
# names.pop(3) # took out tchalla (3rd name in list)
# # del names[0] # deletes name in first index
# fourth = names.op(3) # puts tchala in 'fourth' variable
# # print(names)
# print(fourth)

numbers = []
numbers.insert(0, 1)
numbers.insert(1, 2)
numbers.insert(2, 3)
numbers.insert(3, 4)
numbers.insert(4, 5)
numbers.insert(5, 6)
numbers.pop(0)
numbers[1] = 23
numbers.pop(4)
numbers.insert(2, 5)
print(numbers)

numbers_2 = [2, 3, 4, 5, 6]

numbers_3 = numbers + numbers_2

print(numbers_3) 

# tuple

names = ('tony', 'steve', 'tchala')





