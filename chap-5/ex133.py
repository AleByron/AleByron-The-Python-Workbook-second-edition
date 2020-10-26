def isSublist(smaller, larger):
    a = 0
    b = 0
    c = len(smaller)
    count = 0
    check = 0
    res = False
    while len(larger)>b:
        while len(smaller) > a:
            if smaller[a] == larger[b]:
                count = count + 1
                check = check + 1
                c = 0
            else:
                c = c+1
            a = a + 1
        if check != 0 and check != len(smaller) and c >= len(smaller):
            check = 0
        b = b+1
        a = 0

    if count == len(smaller) and check == len(smaller):
        res = True

  #  print(check)
    return res

def main():
    sm = [0,1,3,4,5]
    lg = [0,1,2,3,4,5,6]
    print(isSublist(sm,lg))

if __name__ == "__main__":
    main()