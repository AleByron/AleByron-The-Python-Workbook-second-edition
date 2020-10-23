y = int(input('Insert an year:'))

if y%400 == 0:
    print('This is a leap year')
elif y%100 == 0:
    print('This is not a leap year')
elif y%4 == 0:
    print('This is a leap year')
else:
    print('This is not a leap year')