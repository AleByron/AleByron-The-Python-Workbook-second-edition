m = float(input('Insert the mass of water you want to heat:'))
T = float(input('How many celsius degrees you want to heat your water?:'))
C = 4.186
q = m*C*T #in Joule
q = abs(q)

2.7777777777777776*10**(-7) #joule to kwh
kwh = q*2.7777777777777776*10**(-7)
cost = kwh*8.9
euro = cost//100
cents = cost-(euro*100)
euro = int(euro)
cents = int(cents)

print('You need',q,'joules, that means',kwh,'kwh','to heat your water, that costs',euro,'euro and',cents,'cents')