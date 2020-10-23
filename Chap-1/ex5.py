small = input("how many one liter bottles you will deposit?: ")
big = input("how many bottles of more than one liter will you deposit?: ")
small = float(small)*0.10
big = float(big)*0.25
total = big+small
print("The total value of your refund is:", total, "$" )