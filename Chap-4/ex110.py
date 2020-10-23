n = int(input('Enter an integer:'))
na = []
na.append(n)
for i in na:
    n = int(input('Enter another integer:'))
    if n == 0:
        break
    na.append(n)


na.sort()
for i in na:
    print(i)

