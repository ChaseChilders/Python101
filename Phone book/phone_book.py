phone_book = []

while True:

  user_input = int(input("""
Electronic Phone Book
=====================
1. Set an entry
2. Look up an entry
3. Delete an entry
4. List all entries
5. Quit

What do you want to do (1-5)?

"""))

  if user_input == 1:
    user_name = input("What is the persons name that you would like to enter ? ")
    user_phone_number = input("What is the persons phone number that you would like to enter? ")
    entered_information = {'Name': user_name, 'Phone Number': user_phone_number}
    phone_book.append(entered_information)
  if user_input == 2:
    searched_name = input("What is the name of the person who's number you are looking for? ")
    for contact in phone_book:
      if searched_name == contact['Name']:
        print(contact)
  if user_input == 3:
    delete_name = input("What is the name of the person who's number you are trying to delete? ")
    for contact in phone_book:
      if delete_name == contact['Name']:
        index = phone_book.index(contact)
        del phone_book[index]
  if user_input == 4:
    print(phone_book)
  if user_input == 5:
    break