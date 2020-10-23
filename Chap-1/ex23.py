import math
n = float(input('Enter the number of sides of your regular polygon:'))
s = float(input('Enter the length of side of your regular polygon:'))
A = (n*(s**2))/4*math.tan(math.pi/n)
print('The area of the polygon is',A)