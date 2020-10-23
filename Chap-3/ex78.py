import math
n = int(input('Enter an int bigger than 0:'))
if n==1:
    print(n)

while n<= 0 or n>=0 and n!=1:
    if n > 0:
        print(n)
        while n != 1:
            if n % 2 == 0:
                n = math.floor(n / 2)
                print(n)
            else:
                n = n * 3 + 1
                print(n)
    else:
        n = int(input('Enter an int bigger than 0:'))
        if n > 0:
            print(n)
            while n != 1:
                if n % 2 == 0:
                    n = math.floor(n / 2)
                    print(n)
                else:
                    n = n * 3 + 1
                    print(n)
