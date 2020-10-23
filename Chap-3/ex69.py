age = str(input('Enter the guest age:'))
group = [] #number of people in str
sum = [] #number of people tranformed in prices
tot = 0 #total price
while age != '':
    group.append(age)
    age = str(input('Enter the guest age:'))

for x in group:
    x = int(x)
    if x <= 2:
        p = 0
        sum.append(p)
    elif 3<= x <= 12:
        p = 14
        sum.append(p)
    elif x >= 65:
        p = 18
        sum.append(p)
    else:
        p=24
        sum.append(p)

for x in sum:
    tot = tot+x

print('The total price is: %.2f' % tot)