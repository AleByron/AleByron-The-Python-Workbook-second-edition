nol = int(input('Insert the number of one day old loans of bread you want to buy:' ))
fullp = nol*3.49
disc = fullp*60/100
tot = fullp - disc
print('The full price of the bread is: %5.2f' % fullp)
print('The discount  is: %5.2f' % disc)
print('The total price of the bread is: %5.2f' % tot)