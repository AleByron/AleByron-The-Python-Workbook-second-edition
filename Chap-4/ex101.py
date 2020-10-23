import random
def plate():
    n = random.randint(0, 1)
    res =''
    x = 1
    if n==0:
        while x<=3:
            a = random.randint(65, 90)
            al = chr(a)
            res = res+al
            x = x+1
        while 4<= x<=6:
            b = random.randint(0, 9)
            b = str(b)
            res = res+b
            x = x+1

    else:
        while x<=4:
            b = random.randint(0, 9)
            b = str(b)
            res = res+b
            x = x+1
        while 5<= x<=7:
            a = random.randint(65, 90)
            al = chr(a)
            res = res+al
            x = x+1

    return res

def main():
    print(plate())

if __name__ == "__main__":
        main()
