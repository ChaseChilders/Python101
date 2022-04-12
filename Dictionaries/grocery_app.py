shopping_list = []

while True:
  user_input = int(input(""" 

===================================
Welcome to the Grocery Shopping App
===================================

1. Add grocery list
2. Add items
3. Delete items
4. View all items
5. Quit

Which one would you like to do? 

"""))

  if user_input == 1:
    list_name = input("What would you like the name of your grocery list to be? ")
  if user_input == 2:
    list_selection = input("What is the name of the grocery list you would like to add to? ")
    list_items = input("What items would you like to add? ")
  if user_input == 3:
    delete_list_selection = input("What is the name  of the list you would like to delete from? ")
    delete_list_items = input("What are the items you would like to delete? ")
  if user_input == 4:
    print(shopping_list)
  if user_input == 5:
    break