year = int(input('Insert an year:'))
x = (2012 - year)%12

if x == 0:
    sign = 'Dragon'
elif x == 11:
    sign = 'Snake'
elif x ==10:
    sign = 'Horse'
elif x == 9 :
    sign = 'Sheep'
elif x == 8:
    sign = 'Monkey'
elif x == 7:
    sign = 'Rooster'
elif x == 6:
    sign = 'Dog'
elif x == 5:
    sign = 'Pig'
elif x == 4:
    sign = 'Rat'
elif x == 3:
    sign = 'Ox'
elif x == 2:
    sign = 'Tiger'
elif x == 1:
    sign = 'Hare'

print(sign)