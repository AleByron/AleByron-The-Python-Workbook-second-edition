dep = float(input("How much your deposit is?: "))
years = int(input("How many years your money will be deposited?: "))
interest = round(dep*4/100, 2)
tot = round(dep+(interest*years), 2)
print("After", years, "years you bank account will be:", tot)