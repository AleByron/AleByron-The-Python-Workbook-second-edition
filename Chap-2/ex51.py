import math
a = float(input('Insert the value A:'))
b = float(input('Insert the value B:'))
c = float(input('Insert the value C:'))

disc = (b**2)-4*a*c
if disc < 0:
    print('There are no real roots')
elif disc == 0:
    root = (-b+math.sqrt((b**2)-4*a*c))/2*a
    print('There is one real root:', root)
elif disc > 0:
    root = (-b+math.sqrt((b**2)-4*a*c))/2*a
    root1 = (-b-math.sqrt((b**2)-4*a*c))/2*a
    print('There are two real roots:',root,root1)
