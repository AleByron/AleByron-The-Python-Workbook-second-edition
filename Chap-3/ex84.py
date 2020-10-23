import random
sum =0
z = 0
while z < 10:
    n = 0 #To count the flips
    q=0 #to break the second while loop
    w=0 #to break the second while loop
    tot ='' #tot of flips
    while q !=3 and w!=3:
        a = random.randint(0, 1)
        if a == 1:
            x = ' H'
            tot = tot + x
            q = q+1
            w = 0
        else:
            x = ' T'
            tot = tot + x
            w = w+1
            q =0
        n = n + 1

    print(tot,'(',n,'flips needed)')
    sum = sum+n
    z = z+1

av = sum/10
print('On average',av,'flips needed')


