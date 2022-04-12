bill_total = int(input("What is the total bill? "))
tip_percentage = int(input("What percentage would you like to tip? "))
number_of_people = int(input("How many people are in your group? "))

def percentage_plus(bill_total, tip_percentage):
  tip_amount = bill_total * (tip_percentage / 100)
  return bill_total + tip_amount

total_cost = percentage_plus(bill_total, tip_percentage)

print(f"Total bill is {total_cost}") 

amount_per_person = total_cost / number_of_people

print(f"Each person should pay {amount_per_person}")
