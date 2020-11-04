def dist(s,t):
    if len(s)==0:
        return len(t)
    elif len(t)==0:
        return len(s)
    else:
        cost = 0
        if s[len(s)-1]!=t[len(t)-1]:
            cost = 1
        d1 = dist(s[0: len(s) - 1], t) + 1
        d2 = dist(s, t[0: len(t) - 1]) + 1
        d3 = dist(s[0: len(s) - 1], t[0: len(t) - 1]) + cost
        return min(d1,d2,d3)

def main():
    s = str(input('Enter the string to transform:'))
    t = str(input('Enter the final string:'))
    print(dist(s,t))

main()