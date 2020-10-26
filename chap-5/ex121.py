import random
lottery = []

while len(lottery) < 7:
    n = random.randint(1,49)
    while n in lottery:
        n = random.randint(1,49)
    lottery.append(n)

lottery.sort()
print(lottery)








