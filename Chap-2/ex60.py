import math
y = int(input('Insert an year:'))
d = (y+math.floor((y-1)/4)-math.floor((y-1)/100)+math.floor((y-1)/400))%7

if d == 6:
    day = 'Saturday'
elif d == 7:
    day = 'Sunday'
elif d == 1:
    day = 'Monday'
elif d == 2:
    day = 'Tuesday'
elif d == 3:
    day = 'Wednesday'
elif d == 4:
    day = 'Thursday'
elif d == 4:
    day = 'Friday'

print(day)