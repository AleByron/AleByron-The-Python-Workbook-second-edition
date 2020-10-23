import random
n = random.randint(0, 38)

if n == 38:
    n = "%02d" % 0
print('The spin resulted in', n)
if n == '00':
    n = 38
if n == 1 or n == 3 or n == 5 or n== 7 or n== 9 or n== 12 or n== 14 or n== 16 or n== 18 or n== 19 or n== 21 or n== 23 or n== 25 or n== 27 or n== 30 or n==32 or n== 34 or n== 36:
    print('Pay red')
if n == 2 or n == 4 or n== 6 or n == 8 or n == 10 or n == 11 or n == 15 or n == 17 or n == 20 or n ==22 or n == 24 or n == 26 or n == 28 or n == 29 or n== 31 or n == 33 or n == 35 or n ==37:
    print('Pay black')
if n%2==0 and n != 0:
    print('Pay even')
if n%2 == 1 and n != 38:
    print('Pay odd')
if 1 <= n <=18:
    print('Pay 1 to 18')
if 19 <= n <= 37:
    print('Pay 19 to 37')
if n == 0 or n == 38:
    print('Pay green')
if n == 38:
    n = "%02d" % 0

print('Pay', n)
