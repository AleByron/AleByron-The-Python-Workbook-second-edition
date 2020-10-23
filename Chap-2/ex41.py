a = float(input('Insert the first side length:'))
b = float(input('Insert the second side length:'))
c = float(input('Insert the third side length:'))
if a == b and b == c:
    print('Your triangle is equilateral')
elif a == b or c == b or a == c:
    print('Your triangle is isosceles')
else:
    print('Your triangle is scalene')