def euclid(a,b):
    if b == 0:
        return a
    else:
        c = a%b
        return euclid(b,c)

def main():
    print(euclid(2570,8394720))

main()
