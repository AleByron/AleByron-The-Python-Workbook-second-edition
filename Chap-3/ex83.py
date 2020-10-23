import random
a = random.randint(0,100)
c = 0
print(a)
for x in range(0,100):
    b = random.randint(0,100)
    if b > a:
        print(b, '<== Update')
        a=b
        c = c+1
    else:
        print(b)

print('the maximum value found is:',a)
print('The value war updated',c,'times')