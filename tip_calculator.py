bill_total = float(input("What is the total bill: "))
tip_percentage = int(input("What percentage would you like to tip? "))

def percentage_plus(bill_total, tip_percentage):
  tip_amount = bill_total * (tip_percentage / 100)
  return bill_total + tip_amount

final_amount = percentage_plus(bill_total, tip_percentage)
print (f"The final amount is {final_amount}")

# def percentage_plus(bill_total, tip_percentage):
#   tip_amount = bill_total * (tip_percentage / 100)
#   return tip_amount + bill_total

# def tip_calculator(bill_total, tip_percentage):
