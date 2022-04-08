# bill_total = float(input("What is the total bill: "))
# tip_percentage = int(input("What percentage would you like to tip? "))

def percentage_plus(bill_total, tip_percentage):
  tip_amount = bill_total * (tip_percentage / 100)
  final_total = bill_total + tip_amount
  return final_total

def tip_calculator():
  bill_total = float(input("What is the total bill: "))
  tip_percentage = int(input("What percentage would you like to tip? "))
  final_total = percentage_plus(bill_total, tip_percentage)
  print(f"Your total is {final_total}")

tip_calculator()

# def percentage_plus(bill_total, tip_percentage):
#   tip_amount = bill_total * (tip_percentage / 100)
#   return tip_amount + bill_total

# def tip_calculator(bill_total, tip_percentage):
