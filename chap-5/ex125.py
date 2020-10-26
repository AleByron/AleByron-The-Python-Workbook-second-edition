import random
def createDeck():
    x = 2
    s = 's'  # spades
    c = 'c'  # clubs
    d = 'd'  # diamonds
    h = 'h'  # hearts
    v = ''
    fig = ['T', 'J', 'Q', 'K', 'A']
    deck = []
    while x < 10:
        x = str(x)
        v = s + x
        deck.append(v)
        v = c + x
        deck.append(v)
        v = d + x
        deck.append(v)
        v = h + x
        deck.append(v)
        x = int(x)
        x = x+1

    for i in range(5):
        v = s + fig[i]
        deck.append(v)
        v = c + fig[i]
        deck.append(v)
        v = d + fig[i]
        deck.append(v)
        v = h + fig[i]
        deck.append(v)

    #print(deck)
    return deck

def shuffle(d):
    deck = d
    x = 0
    import random
    lottery = []
    while len(lottery) < 52:
        n = random.randint(0, 51)
        while n in lottery:
            n = random.randint(0, 51)
        lottery.append(n)

    a = 0
    while x < 52:
        y = deck[x]
        a = random.randint(x,51)
        z = lottery[a]
        deck[x] = deck[z]
        deck[z] = y
        x = x+1

   # print(lottery)
    return deck

def main():
    deck = createDeck()
    s = shuffle(deck)
    print(s)


if __name__ == "__main__":
    main()