import math
radius = float(input('insert the radius of the base of your cylinder: '))
height = float(input('insert the height of your cylinder: '))
base = math.pi*(radius**2)
volume = round(base*height,1)
print('The volume fo your cylinder is', volume)
