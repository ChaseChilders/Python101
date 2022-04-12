# # Dictionary syntax
# # empty
# breakfast_order = {}

# # define data with key and value
# breakfast_order = {
#   "main": "Short Stack",
#   "seat": 3, 
#   "table": 10,
#   "paid": False,
# }

# # access the data inside a dictionary with the key name inside of square brackets

# # print(f'the main for seat {breakfast_order["seat"]} is {breakfast_order["main"]}')

# # access data using value of variable as key
# # table = "main"
# # print(breakfast_order[table])

# breakfast_order["main"] = "Eggs over easy" # reassigning a variable inside breakfast_order
# print(breakfast_order["main"])

# # adding another value to an object (dictionaries)
# breakfast_order["side"] = "hash brown"

# # how to delete an item from a dictionary
# del breakfast_order["side"]

# # nesting data inside dictionaries
# user = {
#   "email": "tony@starkindustries.com",
#   "name": {
#     "first": "Tony",
#     "last": "Stark"
#   }
# }

# # accessing nested data
# first = user['name']['first']
# last = user['name']['last']

# print(f"Hello {user['name']['first']} {user['name']['last']} ")
# print(f"Hello {first} {last}")   

# user = {
#     "name": {
#       "first":"",
#       "last":"",
#   }
# }

# user['name']['first'] = input("What is your first name? ")
# user['name']['last'] = input("What is your last name? ")

# print(f"The name is {user['name']['last']}, {user['name']['first']} {user['name']['last']}")

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

for key in phonebook_dict:
  print(key)
  print(phonebook_dict[key])

print(phonebook_dict['Elizabeth'])

phonebook_dict['Kareem'] = '938-489-1234'

del phonebook_dict['Alice']

phonebook_dict['Bob'] = '968-345-2345'



# ramit = {
#   'name': 'Ramit',
#   'email': 'ramit@gmail.com',
#   'interests': ['movies', 'tennis'],
#   'friends': [
#     { 'name': 'Jasmine', 'email': 'jasmine@yahoo.com', 'interests': ['photography', 'tennis'] },
#     { 'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies', 'tv'] }
#   ]
# }

# print(ramit['email'])

# print(ramit['interests'][0])

# print(ramit['friends'][0]['email'])

# print(ramit['friends'][1]['interests'][1])


# foods = [
#   'pancakes',
#   'waffles',
#   'bagels'
# ]

# orders = {}

# for food in foods:
#   if food not in orders:
#     orders[food] = 0
#   orders[food] = 1

# word_used = {}

# word = input("Please enter a word: ")

# for letters in word:
#   if letters not in word_used:
#     word_used[letters] = 0
#   word_used[letters] += 1

# print(word_used)

# sentence_used = {}

# sentence = input("Please enter a sentence: ")

# x = sentence.split()

# for words in x:
#   if words not in sentence_used:
#     sentence_used[words] = 0
#   sentence_used[words] += 1

# print(sentence_used)

# word_used = {}

# word = input("Please enter a word: ")

# for letters in word:
#   if letters not in word_used:
#     word_used[letters] = 0
#   word_used[letters] += 1

# print(word_used)


# print(sorted_word_used)

# has the top 3 highest used letters
# those top 3 letters need to be ascending value
# which one is the highest number
  #of the highest numbers, which one is highest
    #which one is the next highest
      #which one is the next highest
#Structuring data


# customer = {}