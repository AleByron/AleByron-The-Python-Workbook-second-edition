import random
def randomPass():

    n2 = random.randint(7, 10)
    x = 0
    res = ''
    while x<=n2:
        n1 = random.randint(33, 126)
        a = chr(n1)
        res = res+a
        x = x+1

    return res

def main():
    print(randomPass())

if __name__ == "__main__":
        main()

