import random
from ex146 import bingoCard
from ex147 import checkWinner
#def game():

def main():
    x = 1
    n = []
    while x < 76:
        n.append(x)
        x = x+1

    random.shuffle(n)

    x = 0
    y = 0
    z = 0
    res = 0
    count = []
    while x < 1000:
        a = bingoCard()
        breaker = 0
        for i in n:
            z = z+1
            if breaker == 1:
                count.append(z)
                res = res+z
                break
            for k in a:
                while y < 5:
                    if a[k][y] == i:
                        a[k][y] = 0
                        checkWinner(a)
                    y = y + 1
                if checkWinner(a)==True:
                    breaker = 1
                    break
                y = 0
        x = x+1
        z = 0


    av = res/1000
    M = max(count)
    m = min(count)
    print('The average of calls is:', av, ' while maximum and the minimum calls are: ', M, m)



main()
