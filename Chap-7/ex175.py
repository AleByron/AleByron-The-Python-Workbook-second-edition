def decToBin(a):

    if a == 0 or a == 1:
        return a
    if a < 0:
        return print('The entered value is not a positive integer')
    elif a>=0:
        c = a%2
        b = a // 2
        decToBin(b)
        res = str(c) + str(decToBin(b))
        return res

def main():
    a = int(input('Enter a positive integer:'))
    res = decToBin(a)
    c = len(res)
    counter = -1
    res_new = ''
    for x in res:
        counter = counter + 1
        d = c - counter
        e = c - counter - 1
        f = res[e:d]
        res_new = res_new + f

    print(res_new)
main()