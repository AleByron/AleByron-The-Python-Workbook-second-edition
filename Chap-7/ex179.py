def square(n,g):
    if 0<n-g**2<10**-12:
        return g
    else:
        g = square(n,(g+(n/g))/2)
        return g



def main():
    n = 32
    g = 1
    print(square(n,g))

main()