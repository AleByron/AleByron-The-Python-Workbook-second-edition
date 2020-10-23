x = 1
y = 11
print('    ',end='')
for a in range(x,y):
    print("%4d" % a, end="")
print('\n')

for b in range(x, y):
    print("%4d" % b, end="")
    for c in range(x, y):
        print("%4d" % (b * c), end="")
    print('\n')