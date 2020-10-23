n = int(input('Enter an integer:'))
m = int(input('Enter an integer:'))
a = min(n,m)
b = max(n,m)
d = a
while (a%d==0 and b%d==0) is False:
    d = d-1

print('The greatest common divisor is:',d)