import math
n = int(input('Enter an integer (2 or greater):'))
f = 2
c =1
if n<2:
    print('The number you entered is less then 2')
else:
    while f <= n and c!=n:
        if n % f == 0:
            n = math.floor(n / f)
            print(f)
            c = c*f
        else:
            f = f + 1
