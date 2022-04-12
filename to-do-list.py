# add = int(input("Press 1 to add task: "))
# delete = int(input("Press 2 to delete task: "))
# view_tasks = int(input("Press 3 to view all tasks: "))
# quit_program = input("Press q to quit: ")



# to_do = {
#     "title": ["Mow the lawn", "Wash car", "coding homework"],
#     "priority": ["high", "high", "low"]
# }

# print(to_do['title'][0])

to_do = {
    "title": [''],
    "priority": ['']
  }

user_input = input("Press 1 to add task \nPress 2 to delete task \nPress 3 to view all tasks \nPress q to quit \n: ")
  

if user_input == "1":
    to_do["title"]= input("What is the title of the task? ")
    to_do["priority"]= input("What is the priority of this task? ")
if user_input == "2":
    print(f"{to_do['title']} - {to_do['priority']}")

    # for i, item in enumerate(to_do, 1):
    #   print(i, '- ' + item, sep=' ',end=' ')

# delete task
  # use if statement to print code
  # use the indexing to allow them to select the code they want to delete
  # delete the selected code
  # print the new list of items with the deleted one gone

# print items
  # print the list of current tasks
  # print them by index
  # loop the user input function

# q for quit function

