mpg = float(input('How many miles per gallons run your car?:'))
k = 1.609344 #km in a mile
l = 3.785411784*100 #liters in a gallon
lpk = mpg*l/k #MPG in  KM per lt

print('your car use', lpk, 'Liters per 100Km')