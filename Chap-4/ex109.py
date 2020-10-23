def magic_date(c,m,y):
    m = m.lower()
    if m == 'january':
        d = 1
    elif m == 'february':
        d = 2
    elif m == 'march':
        d = 3
    elif m == 'april':
        d = 4
    elif m == 'may':
        d = 5
    elif m == 'june':
        d = 6
    elif m == 'july':
        d = 7
    elif m == 'august':
        d = 8
    elif m == 'september':
        d = 9
    elif m == 'october':
        d = 10
    elif m == 'november':
        d = 11
    elif m == 'december':
        d = 12

    y = str(y)
    y = y[2:4]
    y = int(y)

    md = d * c

    if y == md:
        e = True
    else:
        e = False

    return e

def main():
    y = int(input('Insert an year:'))
    m = str(input('Insert an month:'))
    d = int(input('Insert a day:'))

    magicday = magic_date(d,m,y)

    if magicday==True:
        print('Hell yes, it is a magic date')
    else:
        print('No man, retry')

main()

