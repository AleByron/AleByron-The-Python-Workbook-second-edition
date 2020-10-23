pur = [4.95, 9.95, 14.95, 19.95, 24.95]
for x in pur:
    disc = round(x*60/100,2)
    price = round(x-disc,2)
    print(x,disc,price)
