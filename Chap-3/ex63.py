
a = int(input('Enter an int value:'))
n = 0
sum = 0
if a != 0:
    while a != 0:
        n = n+1
        sum = sum+a
        a = int(input('Enter another int value:'))
        tot = sum / n
    print(tot)
else:
    print('0 stop the program')








