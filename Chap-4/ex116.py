from ex115 import divisor
def magNum(i):
    pn = 0
    list = divisor(i)
    res = False
    for x in list:
        pn = pn + x
        if pn == i:
            res = True
        else:
            res = False

    return res

def main():
    magicnumbers=[]
    for i in range(1,10000,1):
        a = magNum(i)
        if a == True:
            magicnumbers.append(i)

    print(magicnumbers)

main()
