from ex146 import bingoCard
import random
def checkWinner(card):
    res = 0
    y = 4
    a = 0

    for i in card:
        res = res + card[i][y]
        y = y-1

    if res == 0:
        a = 1
        return True
    else:
        a = 0

    res = 0
    y = 0
    for i in card:
        res = res + card[i][y]
        y = y+1

    if res == 0:
        a = 1
        return True
    else:
        a = 0

    res = 0
    y = 0
    for i in card:
        while y < 5:
            res = res + card[i][y]
            y = y + 1

        if res == 0:
            a = 1
            break
        res = 0
        y = 0

    y = 0
    x = 0
    while x < 5:
        res = 0
        for i in card:
            res = res + card[i][y]

        if res == 0:
            a = 1
            break
        x = x+1
        y = y+1




    if a == 1:
        return True
    else:
        a = 0






def main():
    a = bingoCard()
    b = bingoCard()
    c = bingoCard()
    d = bingoCard()
    e = bingoCard()
    for i in a:
        a[i][1]=0

    x = 0
    while x < 5:
        b['i'][x]= 0
        x = x+1

    x = 0
    for i in c:
        c[i][x] = 0
        x = x+1

    for i in d:
        x = random.randint(0,4)
        d[i][x] = 0

    x = 4
    for i in c:
        e[i][x] = 0
        x = x-1


    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

    print(checkWinner(a))

if __name__ == "__main__":
    main()