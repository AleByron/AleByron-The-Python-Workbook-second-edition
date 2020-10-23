x = 1
pi = 3
z = 0
while x <= 15:
    a = 4/((2+z)*(3+z)*(4+z))
    if x %2 != 0:
        pi = pi + a
    else:
        pi = pi - a

    z = z+2
    x = x + 1
    print(pi)

