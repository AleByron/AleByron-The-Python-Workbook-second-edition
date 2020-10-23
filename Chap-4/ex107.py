
def low_term(n,m):
    a = min(n, m)
    b = max(n, m)
    d = a
    while (a % d == 0 and b % d == 0) is False:
        d = d - 1

    x = int(a / d)
    y = int(b / d)

    return y,x

def main():
    a = int(input('Enter an integer as numerator:'))
    b = int(input('Enter an integer as denominator:'))
    print('The lower terms of your imput is:',low_term(a,b))

if __name__ == "__main__":
        main()