cost = input("What is the total cost of your meal:" )
cost = float(cost)
tax = float(cost*22/100)
tip = float(cost*18/100)
total = cost+tax+tip
print("taxes:", tax)
print("tip:", tip)
print("total:", total)
