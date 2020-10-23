def To10(x,xb):
    b = 0
    z = 0
    tot = 0
    # from any base smaller than 10 to 10
    if xb < 10 and 2 <= xb < 10:
        tot = 0
        c = len(x)
        counter = -1
        x_new = ''
        for a in x:
            counter = counter + 1
            d = c - counter
            e = c - counter - 1
            f = x[e:d]
            x_new = x_new + f
        for a in x_new:
            a = int(a)
            z = a * (xb ** b)
            tot = tot + z
            b = b + 1
    # from any base bigger than 10 to 10
    elif 10 < xb <= 16:
        n = len(x) - 1
        tot = 0
        for a in x:
            if '0' <= a <= '9':
                a = int(a)
                b = a * (xb ** n)
            elif a == 'A':
                a = 10
                b = a * (xb ** n)
            elif a == 'B':
                a = 11
                b = a * (xb ** n)
            elif a == 'C':
                a = 12
                b = a * (xb ** n)
            elif a == 'D':
                a = 13
                b = a * (xb ** n)
            elif a == 'E':
                a = 14
                b = a * (xb ** n)
            elif a == 'F':
                a = 15
                b = a * (xb ** n)
            else:
                print('something went wrong')
                break
            tot = tot + b
            n = n - 1

    return tot

def From10(x,xb,yb):
    # from 10 to any base smaller than 10
    tot = ''
    x = int(x)

    if xb == 10 and 2 <= yb < 10:
        while x != 0:
            b = x % yb
            b = str(b)
            tot = tot + b
            x = x // yb

    elif xb == 10 and 10 < yb <= 16:
        tot = ''
        while x != 0:
            r = x % yb
            r = str(r)
            if r == '10':
                r = 'A'
            elif r == '11':
                r = 'B'
            elif r == '12':
                r = 'C'
            elif r == '13':
                r = 'D'
            elif r == '14':
                r = 'E'
            elif r == '15':
                r = 'F'
            elif '0' <= r <= '9':
                r = r
            else:
                print('something went wrong')
                break
            tot = tot + r
            x = x // yb

    c = len(tot)
    counter = -1
    res_new = ''
    for x in tot:
        counter = counter + 1
        d = c - counter
        e = c - counter - 1
        f = tot[e:d]
        res_new = res_new + f

    tot = res_new

    return tot

def main():
    x = str(input('Enter the first number:'))
    xb = int(input('Enter the base of your first number:'))
    yb = int(input('Enter the base of your second number:'))


    a = To10(x,xb)
    b = From10(a,10,yb)

    print(b)
    return b

if __name__ == "__main__":
        main()














