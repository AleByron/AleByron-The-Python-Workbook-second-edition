x = str(input('Enter a binary number:'))
tot=0
b = 0
z = 0
x_new=''
c = len(x)
counter = -1
for a in x:
    counter = counter + 1
    d = c - counter
    e = c - counter - 1
    f = x[e:d]
    x_new = x_new + f
for a in x_new:
    a = int(a)
    z = a * (2 ** b)
    tot = tot + z
    b = b + 1


print('Decimal number',x,'in binary is',tot)



