def dayInMonth(y,m):
    if y % 400 == 0:
        a = 1
    elif y % 100 == 0:
        a = 0
    elif y % 4 == 0:
        a = 1
    else:
        a = 0
    d = 0
    if m == 1:
        d = 31
    elif m == 2:
        d = 28
        if a == 1:
            d = 29
    elif m == 3:
        d = 31
    elif m == 4:
        d = 30
    elif m == 5:
        d = 31
    elif m == 6:
        d = 30
    elif m == 7:
        d = 31
    elif m == 8:
        d = 31
    elif m == 9:
        d = 30
    elif m == 10:
        d = 31
    elif m == 11:
        d = 30
    elif m == 12:
        d = 31

    return d

def main():
    a = int(input('Insert an year:'))
    b = int(input('Insert an month:'))
    print(dayInMonth(a, b))

if __name__ == "__main__":
        main()
