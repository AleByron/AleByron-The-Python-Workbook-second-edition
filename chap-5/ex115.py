
def divisor(n):
    div = []
    for i in range(n):
        if n % (i + 1) == 0:
            div.append(i + 1)
            
    div.remove(n)
    return div

def main():
    x = int(input('Insert a positive integer:'))
    print(divisor(x))

if __name__ == "__main__":
    main()



