import math
x1 = float(input('Enter the first x-coordinate:'))
y1 = float(input('Enter the first y-coordinate:'))
check = str(x1)
p = 0
while check != '' :
    x2s = str(input('Enter the next x-coordinate (blank to quit):'))
    if x2s != '':
        x2 = float(x2s)
        y2 = float(input('Enter the next y-coordinate :'))
        d = math.sqrt((x2-x1)**2+(y2-y1)**2)
        p = p + d
        x1 = x2
        y1 = y2
        check = x2s
    else:
        check=x2s
print(p)