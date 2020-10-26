def isSorted(x):
    a = x[:]
    a.sort()
    b = a[:]

    b.reverse()

    y = 0
    z = 0
    c = 0
    res = False
    for i in x:
        if a[c] == x[c]:
            y = y + 0
        else:
            y = y + 1
        c = c + 1

    c = 0
    for i in x:
        if b[c] == x[c]:
            z = z + 0
        else:
            z = z + 1
        c = c + 1

    if y + z == 1:
        res = True
    elif y + z == 2:
        res = False
    elif y + z == 0:
        res = True

    print(a,b,x)
    return res

def main():
    lnum= []
    while 0<1:
        a = str(input('Enter a number:'))
        if a == '':
            break
        a = int(a)
        lnum.append(a)

    print(isSorted(lnum))

main()

