x = str(input("Enter the x coordinate of your first point: \n"))
y = str(input("Enter the y coordinate of your first point:\n"))
points = []
points.append(x)
points.append(y)
z = 0
m1 = 0 #sommatory of x*y
mx2 = 0 #sommatory of x
my2 = 0 #sommatory of y
m2 = 0  # product of sommatory x and sommatory y divided by 0
m3 = 0 #sommatory of x**2
m4 = 0 # ((sommatory of x)**2)/n
sy = 0 # summatory of y
sx = 0 # summatory of x
yv = 0 # average y value
xv = 0 # average x value

while points[z]!='':
    x = str(input('Enter the x coordinate of another point:\n'))
    if x == '':
        break
    y = str(input('Enter the y coordinate of another point:\n'))
    points.append(x)
    points.append(y)
    z = z+2

z = 0
while len(points)>z:
    points[z]=float(points[z])
    z = z+1

z = 0
while len(points) > z:
    a = points[z]*points[z+1]
    m1 = m1 + a
    z = z+2

z = 0

while len(points) > z:
    mx2 = mx2 + points[z]
    my2 = my2 +points[z+1]
    z = z+2

m2 = (mx2*my2)/(len(points)/2)
z = 0
while len(points) > z:
    m3 = m3 + points[z]**2
    z = z+2

m4 = ((mx2)**2)/(len(points)/2)

m = (m1 - m2)/(m3-m4)

z = 0
while len(points)>z:
    sx = sx + points[z]
    sy = sy + points[z+1]
    z = z+2

xv = sx/(len(points)/2)
yv = sy/(len(points)/2)

b = sy - m*sx

print( 'With your data y=',m,'* x +',b)






