x = int(input('Insert an amount:'))
if x == 1:
    y = 'George Washington'
elif x ==2:
    y = 'Thomas Jefferson'
elif x ==5:
    y = 'Abraham Lincoln'
elif x ==10:
    y = 'Alexander Hamilton'
elif x ==20:
    y = 'Andrew Jackson'
elif x ==50:
    y = 'Ulysses S. Grant'
elif x ==100:
    y = 'Benjamin Franklin'
else:
    y = 'There is no such note existing'
print(y)