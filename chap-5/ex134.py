def subl(x):
    sl = []
    a = 2
    for c in x:
        sl.append([c])

    while len(x)+1>=a:
        for i in range(0, len(x) - a + 1):
            sl.append(x[i: i + a])
        a = a+1

    sl = sl+[[]]

    return sl

def main():
    l=[1,21,3,41]
    print(subl(l))

if __name__ == "__main__":
    main()