x = float(input('Enter a number:'))
g = x/2
g_e = g*g - x
while g_e >= 10**-12:
    g = (g+x/g)/2
    g_e = g * g - x

print(g)
