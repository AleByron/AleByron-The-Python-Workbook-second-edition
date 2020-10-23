list = []
listn = []
listnmin = []
listn0 = []
listnmaj = []
counter = 0
while counter < 1:
    a = input('Enter an integer: ')
    if a == '':
        counter = 1
    else:
        b = int(a)
        listn.append(b)



for i in listn:
    if i > 0:
        listnmaj.append(i)
    elif i == 0:
        listn0.append(i)
    elif i<0:
        listnmin.append(i)

listn = []

for i in listnmin:
    listn.append(i)

for i in listn0:
    listn.append(i)

for i in listnmaj:
    listn.append(i)

print(listn)


