def romToInt(x):
    dict={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
    res = 0
    if x == '':
        return x
    else:
        if x[0] in dict and len(x)>1:
            if dict[x[0]] >= dict[x[1]]:
                res = dict[x[0]] + romToInt(x[1:])
            elif dict[x[0]] < dict[x[1]]:
                res = romToInt(x[1:]) - dict[x[0]]
        else:
            res = res + dict[x[0]]

        return res



def main():
    x = str(input('Enter a roman number:'))
    print(romToInt(x))
main()