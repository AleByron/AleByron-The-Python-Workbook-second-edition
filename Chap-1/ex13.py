cents = int(input('Insert the amount of money in cents: '))
ton = cents//200

lon = (cents-ton*200)//100

quar = (cents-lon*100-ton*200)//25

dim = (cents-quar*25-lon*100-ton*200)//10

nick = (cents-dim*10-quar*25-lon*100-ton*200)//5

pen = (cents-nick*5-dim*10-quar*25-lon*100-ton*200)//1

print("your change is:",ton,'toonies', lon,'loonies', quar,'quarters', dim, 'dimes', nick, ' nickels', pen, 'pennies')